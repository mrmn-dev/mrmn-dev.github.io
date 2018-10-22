#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mrmn-dev'
SITENAME = u'mrmn-dev'
SITEURL = 'https://mrmn-dev.github.io'
THEME = 'monospace'
MARKDOWN_EXTENSIONS = ['codehilite(css_class=codehilite code)']


PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Hacker News', 'https://news.ycombinator.com/'),)

# Social widget
SOCIAL = (('FiveThirtyEight', 'https://twitter.com/FiveThirtyEight'),
          ('D3.js', 'https://twitter.com/d3js_org?lang=en'),)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
