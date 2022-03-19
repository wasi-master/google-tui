import async_cse

import rich
from rich.columns import Columns
from rich.panel import Panel
from textual import events
from textual.app import App
from textual.widgets import ScrollView
from textual_inputs import TextInput


class GoogleSearchApp(App):
    def __init__(self, token: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.columns = Columns([])
        self.client = async_cse.Search(self.token.split(','))

    async def on_load(self, event: events.Load):
        await self.bind("q", "quit", "Quit")
        await self.bind("enter", "submit", "Submit")

    async def on_mount(self, event: events.Mount) -> None:
        """Create a grid with auto-arranging cells."""
        self.scroll_view = ScrollView(self.columns)
        self.text_input = TextInput(
            name="code",
            title="Search",
        )

        grid = await self.view.dock_grid(edge="left", name="left")

        grid.add_column(fraction=1, name="center")

        grid.add_row(fraction=1, name="top", min_size=3)
        grid.add_row(fraction=10, name="middle")

        grid.add_areas(
            text_view="center,top",
            scroll_view="center,middle",
        )

        grid.place(
            text_view=self.text_input,
            scroll_view=self.scroll_view,
        )

    async def action_submit(self):
        with self.console.status("Searching"):
            search_term = self.text_input.value
            results = await self.client.search(search_term, safesearch=True) # returns a list of async_cse.Result objects
            results_renderables = []
            for result in results:
                results_renderables.append(
                    Panel(
                        f"{result.description or ''}",
                        title=f"[bold blue]{result.title}[/]",
                        title_align="left",
                        border_style="magenta",
                        subtitle=f"[cyan link={result.url}]{result.url}[/]",
                        subtitle_align="right"
                    )
                )
            await self.scroll_view.update(Columns(results_renderables))

    async def on_shutdown_request(self, event) -> None:
        await self.client.close()
        await self.close_messages()

