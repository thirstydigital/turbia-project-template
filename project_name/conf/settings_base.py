"""
Base settings for {{ project_name }}.
"""

import importlib, os, socket, sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

# Add ``python`` folder in home directory to python path.
sys.path.append(os.path.expanduser('~/projects/settings'))

# Add host level settings to local scope as defaults.
locals().update(vars(importlib.import_module(
	'settings.%s' % socket.gethostname().split('.')[0].replace('-', '_'))))

### TURBIA ####################################################################

TURBIA.update({
	'DOCUMENT_ROOT': os.path.join(PROJECT_ROOT, 'public'),
	'PROJECT': os.path.basename(PROJECT_ROOT),
	'PROJECT_ROOT': PROJECT_ROOT,
#	'TEMPLATE_LOADER_CALLBACKS': [
#		'motivate.template.loaders.callback.division_name',
#		'threads.template.loaders.callback.app_name',
#		'threads.template.loaders.callback.namespace',
#		'threads.template.loaders.callback.site_name',
#	],
})

### DJANGO ####################################################################

ADMINS.extend([
#	('Name', 'mailbox@domain.com'),
])

MANAGERS.extend([
#	('Name', 'mailbox@domain.com'),
])

DATABASES = {
	'default': {
		'ATOMIC_REQUESTS': True,
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': TURBIA['PROJECT'],
	}
}

INSTALLED_APPS.extend([
#	'django.contrib.humanize',
#	'django.contrib.messages',

#	'ajax_validation',
#	'debug_toolbar',
#	'haystack',
	'orm_fixtures',
#	'reversion',
#	'tagging',

#	'accounts',
#	'coooeee',
#	'cron',
#	'data',
#	'demo',
#	'dukebox',
#	'fulfilment',
#	'genericforms',
#	'grinner',
#	'mailout',
#	'motivate',
	'pages',
#	'paypal',
#	'permissions',
#	'proxy',
#	'ratings',
#	'reports',
#	'shorten',
#	'sitesettings',
	'textid',
#	'smooth',
#	'threads',
#	'trak',
#	'uniquecodes',

	TURBIA['PROJECT'],
])

MIDDLEWARE_CLASSES.extend([
#	'django.middleware.cache.CacheMiddleware',
#	'django.middleware.gzip.GZipMiddleware',

	# Must come after any middleware that encodes the response, such as
	# GZipMiddleware.
#	'debug_toolbar.middleware.DebugToolbarMiddleware',

#	'demo.middleware.DemoMiddleware',

	# Must come after AuthenticationMiddleware.
#	'motivate.middleware.DivisionMiddleware',

#	'threads.middleware.ThreadLocalAppNameMiddleware',
#	'threads.middleware.ThreadLocalNamespaceMiddleware',
#	'threads.middleware.ThreadLocalRequestMiddleware',
#	'threads.middleware.ThreadLocalSiteMiddleware',

#	'turbia.middleware.CleanQueryMiddleware',
#	'turbia.middleware.P3PHonk',
#	'turbia.middleware.SessionQueryMiddleware',
#	'turbia.middleware.SiteRedirectMiddleware',
])

TEMPLATE_CONTEXT_PROCESSORS.extend([
#	'django.core.context_processors.i18n',
#	'sitesettings.context_processors.sitesettings',
])

TEMPLATE_DIRS = [
	os.path.join(PROJECT_ROOT, 'templates'),
]

TEMPLATE_LOADERS.extend([
#	'turbia.template.loaders.callback.Loader',
#	'django.template.loaders.eggs.Loader',
])

STATICFILES_DIRS = [
	os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_FINDERS.extend([
#	'django.contrib.staticfiles.finders.DefaultStorageFinder',
])

MEDIA_ROOT = os.path.join(TURBIA['DOCUMENT_ROOT'], 'media')
STATIC_ROOT = os.path.join(TURBIA['DOCUMENT_ROOT'], 'static')

WSGI_APPLICATION = '%s.conf.wsgi.application' % TURBIA['PROJECT']
ROOT_URLCONF = '%s.conf.root_urls' % TURBIA['PROJECT']

LOGGING['handlers']['file']['filename'] = \
	os.path.join(PROJECT_ROOT, 'private', 'logs', 'debug.log')

# django.contrib.auth
AUTHENTICATION_BACKENDS.extend([
#	'accounts.backends.ProfileBackend',
])

# django.contrib.sessions
SESSION_SERIALIZER = 'turbia.contrib.sessions.serializers.JSONSerializer'

# django.middleware.cache.CacheMiddleware
#CACHE_BACKEND = 'file://%s/cache' % PROJECT_ROOT
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
#CACHE_MIDDLEWARE_SECONDS = 60 * 10

### HAYSTACK ##################################################################

#HAYSTACK_CONNECTIONS = {
#	'default': {
#		'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#		'URL': 'http://127.0.0.1:8983/solr',
#	},
#}
#HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
