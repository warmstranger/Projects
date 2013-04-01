from django.conf.urls import patterns, url

urlpatterns = patterns('collection.views',
    url(r'^new/collection', 'new_collection'),
    url(r'^create/collection', 'create_collection'),
    url(r'^top/collections$', 'top_collections'),
    url(r'^(?P<username>\w+)/collections$', 'list_collections'),
    url(r'^(?P<username>\w+)/collection/(?P<collection_name>[^/]+)$', 'collection_detail'),
    url(r'^(?P<username>\w+)/collection/(?P<collection_name>[^/]+)/followers$', 'collection_followers'),

    url(r'collection/edit/(?P<collection_id>\d+)$', 'collection_edit'),
    url(r'^(?P<username>\w+)/collection/delete/(?P<collection_id>\d+)$', 'collection_delete'),

)
