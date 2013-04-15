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
    url(r'^post/list/(?P<page>\d+)','post.views.listing'),
    url(r'^post/listing/$','post.views.listing_test'),
    url(r'^post/list_buyer_post/(?P<user_id>\d+)/(?P<page>\d+)','post.views.list_buyer_post'),
    url(r'^post/upload','post.views.upload'),
    url(r'^comment/add/','comment.views.add'),
    url(r'^comment/delete/(?P<id>\d+)','comment.views.delete'),
    url(r'^follow/follow_user/(?P<following_id>\d+)/(?P<user_id>\d+)','follow.views.follow_user'),
    url(r'^follow/unfollow_user/(?P<following_id>\d+)/(?P<user_id>\d+)','follow.views.unfollow_user'),
    url(r'^follow/follow_tag/(?P<following_id>\d+)/(?P<user_id>\d+)','follow.views.follow_tag'),
    url(r'^follow/unfollow_tag/(?P<following_id>\d+)/(?P<user_id>\d+)','follow.views.unfollow_tag'),
    url(r'^feed/(?P<user_id>\d+)','post.views.feed'),
    url(r'^collection/listing/(?P<user_id>\d+)','collection.views.listing'),
    url(r'^collection/collect/(?P<post_id>\d+)/(?P<user_id>\d+)','collection.views.collect'),
    url(r'^collection/cancel_collect/(?P<post_id>\d+)/(?P<user_id>\d+)','collection.views.cancel_collect'),
)
