---
title: Getting started with Ruff and Poetry
date: 2024-04-30
category: Python
tags: [python, ruff, poetry, neovim]
---

I manage most of my Python projects with [Poetry](https://python-poetry.org/), I really
like how it handles dependencies, configures projects and manages virtual environments
using simple commands.

Normally I include linting tools as part of my Poetry projects, specifically
`flake8` and `pylint`. They served me well, but recently I saw a lot of hype
around [ruff](https://docs.astral.sh/ruff/) in online tech circles, so I decided
to give it a try.

And I'm glad I did, ruff and poetry are a match made in heaven. I'm really enjoying
working with ruff, and how I can have really good static code analysis, and really
fast.

In this article, I give a quick guide on how to setup ruff the way I use it on my
Python projects, and how to integrate the `ruff-lsp` to Neovim.

## Add ruff to you poetry dependencies

Assuming you already have a poetry project in place, you can add `ruff` as a 
development dependency:

```bash
poetry add --group dev ruff
```

This will create the following entry in your `pyproject.toml` file:

```toml
[tool.poetry.group.dev.dependencies]
ruff = "^0.4.2"
```

## Configure ruff

The [ruff documentation](https://docs.astral.sh/ruff/configuration/) is pretty
good, and the tool is pretty versatible, so you can set ruff to however you like
on your projects.

You can use a separate file for ruff configurations: `ruff.toml`, however, since
poetry uses `pyproject.toml` for project configuration, we can use that file
to configure `ruff`. I normally use the following configuration parameters on my
project:

```toml
[tool.ruff]
line-length = 120

[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4",  # flake8-comprehensions
    "N",  # PEP8 naming convetions
    "D"  # pydocstyle
]
ignore = [
    "C901",  # too complex
    "W191",  # indentation contains tabs
    "D401"  # imperative mood
]

[tool.ruff.lint.pydocstyle]
convention = "google"
```

Now you can run `poetry run ruff check` on your project and enforce the rules
you want.

## Configure pre-commit checks

I like to add [pre-commit hooks](https://pre-commit.com/) to my repositories. Luckily,
ruff also provies a pre-commit hook, so you can trigger your selected checks every
time you `git commit`. All you need to do is add the following to your
`.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.4.2
  hooks:
    # Run the linter.
    - id: ruff
    # Run the formatter.
    - id: ruff-format
```

You can also enable lint fixes:

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.4.2
  hooks:
    # Run the linter.
    - id: ruff
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
```

*This was taken from [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit)'s
documentation.*

## Configure the ruff Language Server Protocol

*This section is for Neovim, you can find instructions for your editor of choice
on [ruff-lsp docs](https://github.com/astral-sh/ruff-lsp).*

I use [mason.nvim](https://github.com/williamboman/mason.nvim) to manage my LSPs. I'll
probably write an article on how to get all this working on Neovim, but for now, if you
use Mason, you can ensure that `ruff-lsp` is installed:

```lua
require('mason-lspconfig').setup({
    ensure_installed = {
        'pyright',
        'ruff_lsp',
        'rust_analyzer',
        'lua_ls'
    },
    handlers = {
        default_setup,
    },
})
```

I use `ruff-lsp` for linting and formatting, and [pyright](https://github.com/microsoft/pyright)
for everything else, so my setup looks like this;

```lua
-- Ruff for linting and formatting:
require('lspconfig').ruff_lsp.setup {
  init_options = {
    settings = {
      args = {},
    }
  }
}
-- Pyright for everything else:
require('lspconfig').pyright.setup {
    settings = {
        pyright = {
            autoImportCompletion = true,
            -- Using Ruff's import organizer
            disableOrganizeImports = true
        },
        python = {
            analysis = {
                -- Ignore all files for analysis to exclusively use Ruff for linting
                ignore = { '*' }
            }
        }
    }
}
```

I use [venv-lsp.nvim](https://github.com/jglasovic/venv-lsp.nvim) to make sure that
my poetry virtual environment is activated before my LSPs are loaded. For this,
you need to add the following before any LSP configuration:

```lua
-- Activate venv before starting the LSP
require('venv-lsp').init()
```

And that's it! That's the setup I'm running at the moment, I'll update this
guide if I make future improvements.
