from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maimaiti.views.home', name='home'),
    # url(r'^maimaiti/', include('maimaiti.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','post.views.home'),
    url(r'^post/detail/(?P<id>\d+)','post.views.detail'),
    url(r'^post/listing/(?P<page>\d+)','post.views.listing'),
    url(r'^post/upload','post.views.upload'),
    url(r'^comment/add/','comment.views.add'),
    url(r'^comment/delete/(?P<id>\d+)','comment.views.delete'),
)
