import os

import rich_click as click

from .core import GoogleSearchApp

@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option('-t', '--token', required=True, envvar="GOOGLE_API_KEY", help='Google search API token (See documentation for more details)')
def main(token):
    GoogleSearchApp.run(token=token)
