from django.conf.urls import patterns, url

urlpatterns = patterns('tag.views',
    url(r'^top/tags$', 'top_tags'),
    url(r'^(?P<username>\w+)/mentions$', 'list_mentions'),
    url(r'^tag/(?P<tag_name>\S+)$', 'tag_detail'),
)
