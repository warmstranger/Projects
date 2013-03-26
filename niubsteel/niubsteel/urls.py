from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('product.urls')),
    url(r'', include('tag.urls')),
    url(r'', include('collection.urls')),
    url(r'', include('store.urls')),
    url(r'', include('users.urls')),
    url(r'', include('follow.urls')),
    url(r'', include('comment.urls')),
)
