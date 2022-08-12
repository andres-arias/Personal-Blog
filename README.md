# My Personal Website

Built with [Pelican](https://getpelican.com/).
Dependencies managed with [Poetry](https://python-poetry.org/) (try it,
it's awesome!).


## How to build locally

First use `poetry` to install the dependecies:
```
poetry install
```

Then run Pelican with the virtual environment created by Poetry:
```
poetry run pelican -r -l
```
