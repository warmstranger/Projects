from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^register$', 'register'),
    url(r'^login$', 'login'),
    url(r'^weibo_login$','weibo_login'),
    url(r'^wb_callback$','wb_callback'),
    url(r'^taobao_login$','taobao_login'),
    url(r'^tb_callback$','tb_callback'),
    url(r'^logout$', 'logout'),
    url(r'^settings$', 'settings'),
    url(r'^forget/password$', 'forget_password'),
    url(r'^reset/password$', 'reset_password'),
    url(r'^check$', 'check'),
    #url(r'^update_profile', 'update_profile'),
    url(r'^top/users$','top_users'),
    url(r'^weibo_invite$','weibo_invite'),
    url(r'^import_products$','import_products'),

    url(r'^(?P<username>[\d|\w]+)$','profile'),
    url(r'^(?P<username>[\d|\w]+)/followers$','list_followers'),
    url(r'^(?P<username>[\d|\w]+)/followings$','list_followings'),
    url(r'^(?P<username>[\d|\w]+)/following/stores$','list_following_stores'),
)
