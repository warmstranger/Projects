
from django.conf.urls import patterns, url

urlpatterns = patterns('restful.views',
    url(r'^$', 'api_help'),
    url(r'^(?P<api_name>\S*)$', 'api'),
)
