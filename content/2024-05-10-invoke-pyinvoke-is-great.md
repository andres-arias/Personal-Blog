---
title: Invoke (Pyinvoke) is great
date: 2024-05-10
category: Python
tags: [python, invoke, makefile]
---
I recently started using [Invoke](https://www.pyinvoke.org/) to automate common tasks for my projects, such as building and deploying documentation pages. Naturally, I started using Invoke to maintain this blog, so here's a quick guide on how to use Invoke.

## What's invoke?
Invoke is a Python library for managing shell-oriented tasks. It was inspired by Ruby's [Rake](https://ruby.github.io/rake/doc/rakefile_rdoc.html), which is a tool designed to write `Makefiles` using Ruby. The main advantages Rake provided over simple Makefiles is that they are easier to write, and extremely versatile, as you have the whole Ruby programming language to describe tasks.

Invoke is similar to Rake, in that it attempts to provide an alternative to Makefiles for automating tasks. Similarly to Rake, Invoke provides full Python to describe and automate tasks.

## How to use invoke
You first need to install invoke, you can install it globally using `pip`:
```bash
pip install invoke
```

However, and I have written [before](https://andres.world/getting-started-with-ruff-and-poetry), I like to use poetry to manage virtual environments an dependencies, so I just add `invoke` as a "dev" dependency to my projects:

```bash
poetry add --group dev invoke
```

Now that you have invoke available, you need to create a `tasks.py` file on your project's root directory. The `tasks.py` file is invoke's entry point, and can be thought as a `Makefile`, or in the case of rake, as a `Rakefile`.

The `task.py` file is a simple Python script, all you have to do is define functions as tasks using the `@task` decorator:

```python
from invoke import task

@task
def build(c):
    print("Building!")
```

Now the `invoke ` command can be use to call the `build` task:

```bash
$ poetry run invoke build
Building!
```

You can use the `c` variable to run external commands (`c` stands for "context", you can name it however you like, just know that the first parameter will be the "context provider"):

```python
from invoke import task

@task
def build(c):
    c.run("sphinx-build docs docs/_build")
```

```bash
$ poetry run invoke build
Running Sphinx v1.1.3
loading pickled environment... done
...
build succeeded.
```

Follow the [Get Started](https://docs.pyinvoke.org/en/stable/getting-started.html) guide found on invoke's documentation page to learn all the tools invoke provides.

## Bonus: How I manage this blog using invoke

This blog is built using [Pelican](https://andres.world/building-a-blog-with-pelican-and-netlify). Pelican provides a basic [Invoke](https://docs.getpelican.com/en/latest/publish.html#invoke) structure, however, I made some modifications to the `tasks.py` file provided. You can find my [tasks.py](https://github.com/andres-arias/Personal-Blog/blob/main/tasks.py) file on Github.

One of the things I enjoy about invoke is that I can write scripts for anything. For example: I like to name my posts following the convention `YYYY-MM-DD-title-of-post.md`, so I wrote a simple `post` script that asks for a title, category, and tasks, and generates a file following that naming convention, and populates the post's front matter:

```python
from invoke import task

@task
def post(c):
    """
    Generates a new post, following naming conventions.
    """
    title: str = input("Article title: ")
    today_date = datetime.date.today()
    article_name = f"{today_date}-{title.lower().replace(' ', '-')}.md"
    category: str = input("Article category: ")
    tags: list = input("Article tags (comma-separated): ").replace(" ", "").split(",")
    front_matter: str = (
        "---\n"
        f"title: {title}\n"
        f"date: {today_date}\n"
        f"category: {category}\n"
        f"tags: {tags}\n".replace("'", "") + "---\n\n"
    )

    article_path = Path(f"./content/{article_name}")
    if article_path.exists():
        raise FileExistsError(f"File named '{article_name}' already exists!")
    with open(article_path, "w+") as file:
        file.write(front_matter)
    print(f"Article '{article_name}' successfully created!")

```

Now I can just run `poetry run invoke post`, and I get a Markdown file like this one:
```md
---
title: Title of post
date: date: 2024-05-10
category: Python
tags: [python, invoke, poetry]
---

```
