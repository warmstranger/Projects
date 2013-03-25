from django.conf.urls import patterns, url


urlpatterns = patterns('product.views',
    url(r'^$', 'index'),
    url(r'^trending$', 'trending'),
    url(r'^recent$', 'recent_posts'),
    url(r'^popular$', 'popular'),

    url(r'^post/url$', 'post_url'),
    url(r'^post/analyze$', 'post_analyze'),
    url(r'^post/preview$', 'post_preview'),
    url(r'^post/finish$', 'post_finish'),

    url(r'^p/(?P<product_id>\d+)$', 'product_detail'),
    url(r'^p/(?P<product_id>\d+)/(?P<save_id>\d+)$', 'product_save_detail'),
    url(r'^search/', 'search'),

    url(r'^save$', 'save_product'),

    url(r'p/(?P<product_id>\d+)/savers$', 'product_savers'),
)

urlpatterns += patterns('product.robot_view',
    url(r'^robot/push$', 'robot_push'),
)
