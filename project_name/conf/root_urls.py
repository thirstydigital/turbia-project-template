from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.http import Http404
from multiurl import ContinueResolving, multiurl

handler500 = 'turbia.views.server_error_request_context'
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^django-admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^django-admin/',     include(admin.site.urls)),

#	url(r'^accounts/',     include('accounts.urls',     namespace='accounts',     app_name='accounts')),
#	url(r'^coooeee/',      include('coooeee.urls',      namespace='coooeee',      app_name='coooeee')),
#	url(r'^cron/',         include('cron.urls',         namespace='cron',         app_name='cron')),
#	url(r'^data/',         include('data.urls',         namespace='data',         app_name='data')),
#	url(r'^dukebox/',      include('dukebox.urls',      namespace='dukebox',      app_name='dukebox')),
#	url(r'^fulfilment/',   include('fulfilment.urls',   namespace='fulfilment',   app_name='fulfilment')),
#	url(r'^genericforms/', include('genericforms.urls', namespace='genericforms', app_name='genericforms')),
#	url(r'^grinner/',      include('grinner.urls',      namespace='grinner',      app_name='grinner')),
#	url(r'^motivate/',     include('motivate.urls',     namespace='motivate',     app_name='motivate')),
	url(r'^pages/',        include('pages.urls',        namespace='pages',        app_name='pages')),
#	url(r'^paypal/',       include('paypal.urls',       namespace='paypal',       app_name='paypal')),
#	url(r'^proxy/',        include('proxy.urls',        namespace='proxy',        app_name='proxy')),
#	url(r'^ratings/',      include('ratings.urls',      namespace='ratings',      app_name='ratings')),
#	url(r'^reports/',      include('reports.urls',      namespace='reports',      app_name='reports')),
#	url(r'^sitesettings/', include('sitesettings.urls', namespace='sitesettings', app_name='sitesettings')),
#	url(r'^smooth/',       include('smooth.urls',       namespace='smooth',       app_name='smooth')),
#	url(r'^trak/',         include('trak.urls',         namespace='trak',         app_name='trak')),
	url(r'^turbia/',       include('turbia.urls',       namespace='turbia',       app_name='turbia')),
#	url(r'^uniquecodes/',  include('uniquecodes.urls',  namespace='uniquecodes',  app_name='uniquecodes')),

#	url(r'^email/(\d+)-(\w+)/$', 'turbia.views.email',                     name='email'),
	url(r'^static/(.*)$',        'django.contrib.staticfiles.views.serve', name='static'),

	multiurl(
		url(r'^', include('{{ project_name }}.urls', namespace='{{ project_name }}', app_name='{{ project_name }}')),

		url(r'^(.*)$', 'pages.views.page',   name='page'),
		url(r'^(.*)$', 'turbia.views.serve', name='serve'),

		catch=(Http404, ContinueResolving)),
)
