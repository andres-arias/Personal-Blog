---
title: Building a blog with Pelican and Netlify
date: 2022-08-25
category: Web
tags: [Pelican, Python, Netlify]
---

It's been more than a year since I last posted on this website.
I've been busy and I didn't have something to write about, until now.
As I wrote [before](https://andres.world/how-i-got-jekyll-to-work-the-way-i-want.html),
I've been running the classic Jekyll/GitHub Pages combo, but I wanted
to try something different, something that gave me more control over my
website, so I found [Pelican](https://getpelican.com).

Similar to Jekyll, Pelican is a static site generator: its output
are plain HTML/CSS files that you can upload anywhere, you
don't need a backend nor a database. This is great because finding
cheap (free) hosting is easy, and
[Netlify's Started Plan](https://www.netlify.com/pricing/) is perfect
for this type of websites.

Just like Jekyll, Pelican also supports a wide variety of plugins and
themes. The main difference is that Pelican is written in Python, and
being a huge Python fan myself, I decided to give it a go. This is 
the write-up of how I got it working.

## 1. Setup the project using Poetry

I really like [Poetry](https://python-poetry.org/) for managing my
dependencies and virtual environments. 

You can create a new Poetry project by running:
```bash
poetry new new-blog
```

You can find more information on how to use Poetry by reading the
[docs](https://python-poetry.org/docs/basic-usage/).

Now you can start with a simple `pyproject.toml` file containing
some dependencies:

```toml
[tool.poetry]
name = "pelican-blog"
version = "0.1.0"
description = ""
authors = ["Andres Arias"]

[tool.poetry.dependencies]
python = "^3.9"
pelican = {extras = ["markdown"], version = "^4.8.0"}
ipython = "^8.4.0"
pelican-liquid-tags = "^1.0.3"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

For those wondering why I'm pulling `ipython` and `pelican-liquid-tags`: 
this is for enabling IPython support on my (future) posts. I don't
know if I'll ever need it, but it might come in handy if I ever
need to share a plot or two.

Then I can just run
```bash
poetry install
```

to create a new virtual environment and populate it with my dependencies.

**(OPTIONAL)** you can use Git submodules to add the
[pelican-themes](https://github.com/getpelican/pelican-themes) and
[pelican-plugins](https://github.com/getpelican/pelican-plugins) repos to your
projects without having to push everything to your repo:
```bash
git submodule add https://github.com/getpelican/pelican-themes.git theme
git submodule add https://github.com/getpelican/pelican-plugins.git plugins
```

This way, you have plenty of plugins and themes quickly available for you.

## 2. Configure your blog

Your main point of configuration will be the `pelicanconf.py` file. All the
configuration options are described on the 
[Pelican docs](https://docs.getpelican.com/en/latest/settings.html).

[Here](https://github.com/andres-arias/Personal-Blog/blob/main/pelicanconf.py) 
you can find my configuration file.

## 3. Kickstart your website

Once everything's installed, you can run the following command
to build a basic Pelican structure:
```bash
poetry run pelican-quickstart
```

And the you can run:
```bash
poetry run pelican -r -l
```
to serve a local copy of your site. And when you're done, you can run
```bash
poetry run make html
```
to build the resulting website that you can deploy to your hosting
service of choice, or if you keep reading, you can deploy it automatically
to Netlify every time you commit changes to you git repo.

## 3. Setup Netlify to automatically deploy your website

In order to automatically deploy your website you need two files:

**runtime.txt**: Indicates the Python version to run. Here's a
[list](https://github.com/netlify/build-image/blob/focal/included_software.md) 
of available runtimes. Since Python 3.8 is the latest available (as the 
time I'm writing this), this is the one I'll be using. Just create a file
named `runtime.txt` in your project's root directory containing the runtime
version:
```
3.8
```

**netlify.toml**: Contains the steps required to build your website. For
our Pelican project, the `netlify.toml` file would be:
```toml
[build]
publish = "output"
command = """
pip install -q poetry &&
poetry config virtualenvs.in-project true &&
poetry install -v &&
poetry run make html
"""
```

This means that every time we push changes, Netlify will install poetry,
create the virtual environment,  download the dependencies and build
the resulting HTML files.

Once this is all set, just point your Publish directory in Netlify to
the `output/` folder and link it to your Github repo.

That's it! Now every time you commit something, Netlify will automatically
pull the new changes and deploy them.

That's all for now, thank you for reading and I hope this was useful.
