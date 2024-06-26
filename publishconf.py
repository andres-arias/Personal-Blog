import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://andres.world"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

SEO_REPORT = True
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True
