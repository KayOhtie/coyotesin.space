from datetime import date

AUTHOR = 'Kay Ohtie'
SITENAME = 'Coyotes in Space'
SITEURL = ''
SITE_DOMAIN = 'coyotesin.space'
CURRENT_YEAR = date.today().year

PATH = 'content'
STATIC_PATHS = ['images','files','.well-known','_config.yml']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{slug}.html'
ARTICLE_URL = 'articles/{date:%Y}/{slug}.html'
INDEX_SAVE_AS = 'articles/index.html'
#TEMPLATE_PAGES = { 'pages/proof.md':'proof.md.asc.txt' }
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

THEME="themes/yotespace"
THEME_STATIC_DIR = ''
THEME_STATIC_PATHS = ['static','source/font-awesome/webfonts']
CSS_FILE = 'main.css'
WEBASSETS_SOURCE_PATHS = ['node_modules','../../node_modules']

#PLUGIN_PATHS = ["plugins"]
PLUGINS=['pelican.plugins.webassets', 'pelican.plugins.pelimoji']
#PLUGINS=['pelican.plugins.webassets']


# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Mastodon', 'https://blimps.xyz/@KayOhtie'),
    ('GitHub', 'https://github.com/Ceralor'),
    ('Keyoxide', 'https://keyoxide.org/hkp/EF9328927969D342939BBB2718817244ED315340'),
	#('FurAffinity','https://furaffinity.net/user/ceralor'),
    ('KoFi','https://ko-fi.com/kayohtie')
)

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True