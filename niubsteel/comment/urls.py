from django.conf.urls import patterns, include, url

urlpatterns = patterns('comment.views',
    url(r'^p/comment/(?P<product_id>\d+)$', 'save_comment'),
    url(r'^p/comments/(?P<product_id>\d+)$', 'list_comments'),
)
