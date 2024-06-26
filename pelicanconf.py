AUTHOR = 'Andrés Arias'
SITENAME = "Andrés' Blog"
SITEURL = 'https://andres.world'
PATH = 'content'
TIMEZONE = 'America/Costa_Rica'
DEFAULT_LANG = 'en'

ABOUT_ME = "I'm a Computer Engineer from Costa Rica working as an Embedded "\
    "Software Engineer. Here I write about the experiments I'm working on and "\
    "the things I learn."

CUSTOM_LICENSE = 'Content licensed under <a href="https://creativecommons.org/licenses/by/4.0/"'\
        'target="_blank">CC BY 4.0</a>, except where indicated otherwise.'
THEME = 'themes/pelican-bootstrap3/'
PLUGIN_PATHS = ['plugins/']
PLUGINS = [
    'i18n_subsites',
    'seo'
]
LIQUID_TAGS = ["notebook"]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

STATIC_PATHS = [
    'images',
    'extra'
]

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

# Enable archives page
ARCHIVES_SAVE_AS = 'archives.html'

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True
