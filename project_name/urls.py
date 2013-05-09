from django.conf.urls import include, patterns, url
from django.http import Http404

urlpatterns = patterns('{{ project_name }}.views',
#	url(r'^$', 'index', name='index'),
)

urlpatterns += patterns('',
#	url(r'^admin/', include('{{ project_name }}.admin.views', namespace='{{ project_name }}-admin', app_name='{{ project_name }}'),
#	url(r'^(.*)$', 'pages.views.page', name='page'),
)
