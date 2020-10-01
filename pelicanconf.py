#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = 'Kay Ohtie'
SITENAME = 'Coyotes in Space'
SITEURL = ''
TWITTER_USERNAME = '@ceralor'
CURRENT_YEAR = date.today().year

PATH = 'content'
STATIC_PATHS = ['images','files','.well-known']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
INDEX_SAVE_AS = 'blog_index.html'
TEMPLATE_PAGES = { 'pages/proof.md':'proof.md.asc.txt' }
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives', 'tag']
PAGINATED_TEMPLATES = {'index':None, 'tags': None, 'categories': None, 'archives': None, 'tag': None}


TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'
LOCALE="en_US.UTF-8"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS=['assets', 'pelimoji', 'simple-fa']
#PELIMOJI_PATH = 'images/emoji'


THEME="theme"
THEME_STATIC_DIR = ''
THEME_STATIC_PATHS = ['static','source/font-awesome/webfonts']
CSS_FILE = 'main.css'

# Blogroll
LINKS = (('Keybase', 'https://keybase.io/ceralor'),
	('Github', 'https://github.com/ceralor'),
	('BitBucket', 'https://bitbucket.com/ceralor'))

# Social widget
SOCIAL = (('Mastodon', 'https://blimps.xyz/@ceralor'),
	('Fur Affinity','https://furaffinity.net/user/ceralor'),
	('Twitter','https://twitter.com/ceralor'))

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
