from django.conf.urls import patterns, url

urlpatterns = patterns('users.views',
    url(r'^login$', 'login'),
    url(r'^login/connector/(?P<connector_name>\w+)', 'connector_login'),
    url(r'^login/callback/(?P<connector_name>\w+)', 'connector_callback'),
    url(r'^convert$', 'convert'),
    url(r'^connector/cancel/(?P<connector_name>\w+)', 'connector_cancel'),
    url(r'^connector/(?P<connector_name>\w+)/(?P<uid>\d+)', 'connector_detail'),

    url(r'^register$', 'register'),
    url(r'^logout$', 'logout'),
    url(r'^logout_login$', 'logout_login'),
    url(r'^settings$', 'settings'),
    url(r'^forget/password$', 'forget_password'),
    url(r'^reset/password$', 'reset_password'),
    url(r'^check$', 'check'),
    url(r'^top/users$','top_users'),

    url(r'^(?P<username>[\d|\w]+)$','profile'),
    url(r'^(?P<username>[\d|\w]+)/followers$','list_followers'),
    url(r'^(?P<username>[\d|\w]+)/followings$','list_followings'),
    url(r'^(?P<username>[\d|\w]+)/following/stores$','list_following_stores'),
)
