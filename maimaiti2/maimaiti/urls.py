from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login', 'users.views.login'),
    url(r'^redirect_logout', 'users.views.logout'),
    url(r'^redirect_login', 'users.views.redirect_login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('restful.urls')),
    url(r'^', 'static.views.index'),
)
