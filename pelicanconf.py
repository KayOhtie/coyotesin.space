#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kay'
SITENAME = 'Coyotes in Space'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['blog','images']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS=['assets','gallery']

THEME="theme"

TEMPLATE_PAGES = { 'pages/kaypics.html': 'kaypics.html'}
LINKS = ()
# Blogroll
#LINKS = (('Keybase', 'https://keybase.io/ceralor'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Mastodon', 'https://blimps.xyz/@ceralor'),
	('Fur Affinity','https://furaffinity.net/user/ceralor'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
