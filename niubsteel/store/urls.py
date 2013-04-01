from django.conf.urls import patterns, url

urlpatterns = patterns('store.views',
    url(r'^top/stores$', 'top_stores'),
    url(r'^store/(?P<store_name>\S*)$', 'store_detail'),
    url(r'^(?P<username>\w+)/stores$', 'list_stores'),
)
