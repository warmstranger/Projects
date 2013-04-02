from django.conf.urls import patterns, url

urlpatterns = patterns('store.views',
    url(r'^top/stores$', 'top_stores'),
    url(r'^store/(?P<store_name>[\w\d.-]+)$', 'store_detail'),
    url(r'^(?P<username>\w+)/stores$', 'list_stores'),
    url(r'^stores/(?P<store_name>[\w\d.-]+)/claim/new$', 'store_claim'),
    url(r'^stores/(?P<store_name>[\w\d.-]+)/followers$', 'store_followers'),
)
