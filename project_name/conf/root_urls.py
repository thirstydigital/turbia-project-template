from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.http import Http404
from multiurl import ContinueResolving, multiurl

handler500 = 'turbia.views.server_error_request_context'
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('{{ project_name }}.urls')),

	url(r'^django-admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^django-admin/',     include(admin.site.urls)),

#	url(r'^accounts/',     include('accounts.urls')),
#	url(r'^coooeee/',      include('coooeee.urls')),
#	url(r'^cron/',         include('cron.urls')),
#	url(r'^data/',         include('data.urls')),
#	url(r'^demo/',         include('demo.urls')),
#	url(r'^dukebox/',      include('dukebox.urls')),
#	url(r'^fulfilment/',   include('fulfilment.urls')),
#	url(r'^genericforms/', include('genericforms.urls')),
#	url(r'^grinner/',      include('grinner.urls')),
#	url(r'^mailout/',      include('mailout.urls')),
#	url(r'^motivate/',     include('motivate.urls')),
	url(r'^pages/',        include('pages.urls')),
#	url(r'^paypal/',       include('paypal.urls')),
#	url(r'^proxy/',        include('proxy.urls')),
#	url(r'^reports/',      include('reports.urls')),
#	url(r'^shorten/',      include('shorten.urls')),
#	url(r'^sitesettings/', include('sitesettings.urls')),
#	url(r'^smooth/',       include('smooth.urls')),
#	url(r'^trak/',         include('trak.urls')),
	url(r'^turbia/',       include('turbia.urls')),
#	url(r'^uniquecodes/',  include('uniquecodes.urls')),

	url(r'^e-(\d+)-(\w+)/$', 'turbia.views.email', name='turbia_email'),
#	url(r'^s-(\w{3,})/$',    'shorten.views.link', name='shorten_link'),

	url(r'^static/(.*)$', 'django.contrib.staticfiles.views.serve', name='static'),

	multiurl(
		url(r'^(.*)$', 'pages.views.page',   name='page'),
		url(r'^(.*)$', 'turbia.views.serve', name='serve'),

		catch=(Http404, ContinueResolving)),
)
