from django.conf.urls import patterns, url

urlpatterns = patterns('tree.views',
    url(r'tree^$', 'home'),
)