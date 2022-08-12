AUTHOR = 'Andrés Arias'
SITENAME = 'Random Computer Blog'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Costa_Rica'
DEFAULT_LANG = 'en'

ABOUT_ME = "I'm a Computer Engineer from Costa Rica working as an Embedded "\
    "Software Engineer. Here I write about the experiments I'm work on and "\
    "the things I learn."

CC_LICENSE = "BY-SA"

THEME = 'themes/pelican-bootstrap3/'
PLUGIN_PATHS = ['plugins/']
PLUGINS = [
    'i18n_subsites'
]
LIQUID_TAGS = ["notebook"]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Template settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 200

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://www.linkedin.com/in/andresarias95/'),
    ('Github', 'https://github.com/andres-arias')
)

MENUITEMS = [
    ('Categories', '/categories.html')
]

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
