# -*- coding: utf-8 -*-

import datetime
import os
import shlex
import shutil
from pathlib import Path

from invoke import task
from invoke.main import program
from livereload import Server
from pelican import main as pelican_main
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = True
SETTINGS_FILE_BASE = "pelicanconf.py"
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)

CONFIG = {
    "settings_base": SETTINGS_FILE_BASE,
    "settings_publish": "publishconf.py",
    "deploy_path": SETTINGS["OUTPUT_PATH"],
    "host": "localhost",
    "port": 8000,
}


@task
def clean(c):
    """
    Remove generated files
    """
    if os.path.isdir(CONFIG["deploy_path"]):
        shutil.rmtree(CONFIG["deploy_path"])
        os.makedirs(CONFIG["deploy_path"])


@task
def build(c):
    """Build local version of site"""
    pelican_run("-s {settings_base}".format(**CONFIG))


@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run("-d -s {settings_base}".format(**CONFIG))


@task
def serve(c):
    """Automatically reload browser tab upon file modification."""

    def cached_build():
        cmd = "-s {settings_base} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true"
        pelican_run(cmd.format(**CONFIG))

    cached_build()
    server = Server()
    theme_path = SETTINGS["THEME"]
    watched_globs = [
        CONFIG["settings_base"],
        "{}/templates/**/*.html".format(theme_path),
    ]

    content_file_extensions = [".md", ".rst"]
    for extension in content_file_extensions:
        content_glob = "{0}/**/*{1}".format(SETTINGS["PATH"], extension)
        watched_globs.append(content_glob)

    static_file_extensions = [".css", ".js"]
    for extension in static_file_extensions:
        static_file_glob = "{0}/static/**/*{1}".format(theme_path, extension)
        watched_globs.append(static_file_glob)

    for glob in watched_globs:
        server.watch(glob, cached_build)

    if OPEN_BROWSER_ON_SERVE:
        # Open site in default browser
        import webbrowser

        webbrowser.open("http://{host}:{port}".format(**CONFIG))

    server.serve(host=CONFIG["host"], port=CONFIG["port"], root=CONFIG["deploy_path"])


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


def pelican_run(cmd):
    cmd += " " + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))
