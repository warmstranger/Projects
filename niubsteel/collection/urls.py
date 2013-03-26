from django.conf.urls import patterns, url

urlpatterns = patterns('collection.views',
    url(r'^new/collection', 'new_collection'),
    url(r'^top/collections$', 'top_collections'),
    url(r'^(?P<username>\w+)/collections$', 'list_collections'),
    url(r'^(?P<username>\w+)/collection/(?P<collection_name>\w+)$', 'collection_detail'),

    # use collection name in the url may have problem.
    url(r'^(?P<username>\w+)/collections/(?P<collection_id>\d+)$', 'get_collection'),
)
