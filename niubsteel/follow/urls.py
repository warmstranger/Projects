from django.conf.urls import patterns, url

urlpatterns = patterns('follow.views',
    url(r'^follow/(?P<username>\w+)/collection/(?P<collection_name>\w+)$', 'follow_collection'),
    url(r'^follow/store/(?P<store_name>[\w\d.-]+)$', 'follow_store'),
    url(r'^follow/tag/(?P<tag_name>\S+)$', 'follow_tag'),
    url(r'^follow/(?P<username>[\d|\w]+)$','follow_user'),
)
