# google-tui

A textual user interface for [google.com](https://www.google.com)

## Prerequisites **(❗Read carefully❗)**

Firstly, you'll need to install the package

```sh
pip install google-tui
```

Secondly, you'll need to get google search api key(s)

1. Go to [developers.google.com/custom-search/v1/overview](https://developers.google.com/custom-search/v1/overview)
2. Scroll down
3. Click the big blue `Get a key` button ([screenshot](https://camo.githubusercontent.com/f784b64d7d88eb113230ce9c02b10df810262debfc35e64b3eaf79ca83ac45b4/68747470733a2f2f6d69786564616e616c79746963732e636f6d2f626c6f672f77702d636f6e74656e742f75706c6f6164732f676f6f676c652d7365617263682d6170692d696d67312e6a7067)])
4. Make a app if you haven't already, the name doesn't matter
5. Click the `NEXT` button
6. You'll get an api key

You can do the above process as many times as you want. Each api key has a 100 request limit per day, which is plenty for normal use but if you ever run out of uses you can just create more api keys

Thirdly, you'll need to provide the token(s) to the package.  You can use a environment variable named `GOOGLE_API_KEY` or you can pass the token(s) directly with the `--token`/`-t` flag. The environment variable/flag value should be comma separated without spaces (e.g. `a,b,c`) for multiple tokens or just a singe token (`a`).

Then you can go in a terminal and run

```sh
google-tui
```

And that should work, otherwise try

```sh
python -m google_tui
```

