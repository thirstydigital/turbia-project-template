"""
Safe default settings.
"""

import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

### TURBIA SETTINGS ###########################################################

TURBIA = {
	'CATCH_ALL_VIEWS': [
#		'pages.views.page',
#		'turbia.views.serve',
	],
	'CONTEXT_SETTINGS': [
		'INSTALLED_APPS',
		'ROOT_URL',
	],
	'DOCUMENT_ROOT': os.path.join(PROJECT_ROOT, 'public'),
#	'DOMAIN': 'localhost:8000',
	'MASTER_PASSWORDS': {
#		'abc123': lambda u: not (u.is_staff or u.is_superuser),
	},
	'PROJECT': os.path.basename(PROJECT_ROOT),
	'PROJECT_ROOT': PROJECT_ROOT,
	'RECAPTCHA': {
		'PRIVATE_KEY': '',
		'PUBLIC_KEY': '',
	},
#	'REDIRECT_EMAIL': True,
#	'REDIRECT_EMAIL_RECIPIENTS': [],
#	'REDIRECT_SMS': True,
#	'REDIRECT_SMS_RECIPIENTS': [],
	'ROOT_URL': '/',
#	'SEND_EMAIL': False,
#	'SEND_SMS': False,
	'SMS': {
		'default_gateway': 'dialect-interactive',
		'dialect-interactive': {
			'username': '30thirty',
			'password': 'th1r74',
		},
	},
	'TEMPLATE_LOADER_CALLBACKS': [
#		'motivate.template.loaders.callback.division_name',
#		'threads.template.loaders.callback.app_name',
#		'threads.template.loaders.callback.namespace',
#		'threads.template.loaders.callback.site_name',
	],
	'TEXTIMAGE': {
		'FONT_PATH': os.path.join(PROJECT_ROOT, 'private', 'fonts'),
		'MAP': {
#			'alias': [
#				'font', 'size', 'foreground', 'background', 'hover_foreground',
#				'hover_background', 'charset'],
		},
	},
}

### COOOEEE SETTINGS ##########################################################

COOOEEE = {
	'bounce': {
		'protocol': 'IMAP',
		'host': 'imap.gmail.com',
		'user': 'bounce@3030.com.au',
		'password': '80unc3',
		'use_ssl': True,
		'trash_mailbox': '[Gmail]/Trash',
#		'email': None,
	},
	'unsubscribe': {
		'protocol': 'IMAP',
		'host': 'imap.gmail.com',
		'user': 'unsubscribe@3030.com.au',
		'password': 'un5u85cr183',
		'use_ssl': True,
		'trash_mailbox': '[Gmail]/Trash',
#		'email': None,
	},
}

### DEMO SETTINGS #############################################################

def CALLBACK(request):
	"""
	Returns True when conditions for skipping demo check are met.
	"""
	if request.user.is_superuser:
		return True

	exts = [
		'css',
		'gif',
		'ico',
		'jpg',
		'js',
		'png',
	]
	ext = request.path.split('.')[-1]
	if ext in exts:
		return True

	apps = ['admin']
	urls = ['demo_login', 'turbia_login']
	try:
		resolver_match = resolve(request.path)
	except Http404:
		return False
	return (resolver_match.app_name in apps or resolver_match.url_name in urls)

DEMO = {
	'ENABLE': False,
	'TOKEN': '_turbia_demo_token',
	'CALLBACK': CALLBACK,
}

### DJANGO SETTINGS ###########################################################

ADMINS = [
	('Admin', 'admin@3030.com.au'),
]
MANAGERS = [
	('Manager', 'admin@3030.com.au'),
	('Support', 'support@3030.com.au'),
]

#DEBUG = False
#TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
	'.3030.com.au',
	'.localhost',
]

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': TURBIA['PROJECT'],
	}
}

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.auth',
	'django.contrib.contenttypes',
#	'django.contrib.humanize',
#	'django.contrib.messages',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.staticfiles',

#	'ajax_validation',
#	'debug_toolbar',
#	'haystack',
#	'reversion',
	'south',
	'django_nose', # must come after south.
#	'tagging',

	'turbia',

#	'accounts',
#	'coooeee',
#	'cron',
#	'data',
#	'demo',
#	'dukebox',
#	'fulfilment',
#	'genericforms',
#	'grinner',
#	'motivate',
	'pages',
#	'paypal',
#	'permissions',
#	'proxy',
#	'ratings',
#	'reports',
#	'shorten',
#	'sitesettings',
#	'smooth',
#	'threads',
#	'trak',
#	'uniquecodes',

	TURBIA['PROJECT'],
]

MIDDLEWARE_CLASSES = [
	# Must come before AuthenticationMiddleware.
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
#	'django.middleware.cache.CacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.doc.XViewMiddleware',
#	'django.middleware.gzip.GZipMiddleware',

	# Must come after any middleware that encodes the response, such as
	# GZipMiddleware.
#	'debug_toolbar.middleware.DebugToolbarMiddleware',

	'django.middleware.transaction.TransactionMiddleware',

	# Must come after AuthenticationMiddleware.
#	'motivate.middleware.DivisionMiddleware',

#	'threads.middleware.ThreadLocalAppNameMiddleware',
#	'threads.middleware.ThreadLocalNamespaceMiddleware',
#	'threads.middleware.ThreadLocalRequestMiddleware',
#	'threads.middleware.ThreadLocalSiteMiddleware',
	'turbia.alerts.AlertMiddleware',
#	'turbia.middleware.CleanQueryMiddleware',
#	'turbia.middleware.P3PHonk',
#	'turbia.middleware.SessionQueryMiddleware',
	'turbia.middleware.SiteMiddleware',
#	'turbia.middleware.SiteRedirectMiddleware',

#	'demo.middleware.DemoMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
#	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
	'django.core.context_processors.static',
#	'sitesettings.context_processors.sitesettings',
	'turbia.context_processors.device',
	'turbia.context_processors.next',
	'turbia.context_processors.path_fragments',
	'turbia.context_processors.referer',
	'turbia.context_processors.site',
	'turbia.context_processors.user_agent',

	# put this last if you want to override context variables generated by
	# other context processors.
	'turbia.context_processors.context_settings',
]

TEMPLATE_DIRS = [
	os.path.join(PROJECT_ROOT, 'templates'),
]

TEMPLATE_LOADERS = [
#	'turbia.template.loaders.callback.Loader',
	'turbia.template.loaders.static.Loader',
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	'django.template.loaders.eggs.Loader',
]

WSGI_APPLICATION = '%s.conf.wsgi.application' % TURBIA['PROJECT']
ROOT_URLCONF = '%s.conf.root_urls' % TURBIA['PROJECT']

# Detect HTTPS requests that have been through a proxy.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# Get the secret key from a hidden file that should never be committed to
# version control. If it doesn't exist, create it.
SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
try:
	SECRET_KEY = open(SECRET_FILE).read().strip()
except IOError:
	try:
		import string, random
		SECRET_CHARSET = ''.join([
			string.digits, string.ascii_letters, string.punctuation])
		SECRET_KEY = ''.join(random.choice(SECRET_CHARSET) for i in range(50))
		secret = open(SECRET_FILE, 'w')
		secret.write(SECRET_KEY)
		secret.close()
		os.chmod(SECRET_FILE, 0400)
	except IOError:
		raise Exception(
			'Please create a %s file with 50 random characters to set your '
			'secret key.' % SECRET_FILE)

LANGUAGE_CODE = 'en-au'
TIME_ZONE = 'Australia/Sydney'

DATE_FORMAT = 'D, j M Y'
TIME_FORMAT = 'g:i A'
DATETIME_FORMAT = '%s, %s' % (DATE_FORMAT, TIME_FORMAT)

DAY_FORMAT = 'D'
HOUR_FORMAT = 'g A'

MEDIA_ROOT = os.path.join(TURBIA['DOCUMENT_ROOT'], 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(TURBIA['DOCUMENT_ROOT'], 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
	os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_FINDERS = [
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#	'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

LOGIN_REDIRECT_URL = '/turbia/'
LOGIN_URL = '/turbia/login/'
LOGOUT_URL = '/turbia/logout/'

DEFAULT_FROM_EMAIL = 'noreply@3030.com.au'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#EMAIL_HOST = 'mail.internode.on.net'

DEFAULT_FILE_STORAGE = 'turbia.core.files.storage.FileSystemStorage'
FILE_UPLOAD_PERMISSIONS = 0644

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'color': {
			'()': 'turbia.logging.ColorFormatter',
			'format': '[%(levelname)s] %(message)s',
		},
	},
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse',
		},
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'color',
		},
		'file': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': os.path.join(
				PROJECT_ROOT, 'private', 'logs', 'debug.log'),
			'maxBytes': 100000,
			'backupCount': 1,
		},
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		},
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		'turbia': {
			'handlers': ['file'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}

# django.contrib.auth
AUTHENTICATION_BACKENDS = [
#	'accounts.backends.ProfileBackend',
	'turbia.auth.MasterPasswordBackend',
]

# django.contrib.sites
SITE_ID = 1

# django.core.context_processors.i18n
USE_I18N = False

# django.middleware.cache.CacheMiddleware
#CACHE_BACKEND = 'file://%s/cache' % PROJECT_ROOT
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_SECONDS = 60 * 10

# django.middleware.common.CommonMiddleware
USE_ETAGS = True

### DJANGO DEBUG TOOLBAR SETTINGS #############################################

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PANELS = [
	'debug_toolbar.panels.version.VersionDebugPanel',
	'debug_toolbar.panels.timer.TimerDebugPanel',
	'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
	'debug_toolbar.panels.headers.HeaderDebugPanel',
	'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
	'debug_toolbar.panels.template.TemplateDebugPanel',
	'debug_toolbar.panels.sql.SQLDebugPanel',
	'debug_toolbar.panels.signals.SignalDebugPanel',
	'debug_toolbar.panels.logger.LoggingPanel',
]
INTERNAL_IPS = [
	'127.0.0.1',
	'59.167.247.200',
]
# backwards compatibility.
DATABASE_ENGINE = DATABASES['default']['ENGINE']

### HAYSTACK SETTINGS #########################################################

#HAYSTACK_SITECONF = 'conf.search_sites'
#HAYSTACK_SEARCH_ENGINE = 'solr' # solr, woosh, xapian, dummy
#HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr'
#HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'whoosh', 'index')

### NEW RELIC SETTINGS ########################################################

NEWRELIC_ENV = 'development'

### NOSE SETTINGS #############################################################

NOSE_ARGS = [
	'--cov-report=html', '--cov-report=term', '--logging-clear-handlers',
	'--with-progressive']

### PAGES SETTINGS ############################################################

PAGES = {
	'CLOSURE_COMPILATION_LEVEL': 'SIMPLE_OPTIMIZATIONS',
	'MINIFY-CSS': True,
	'MINIFY-JS': True,
}
