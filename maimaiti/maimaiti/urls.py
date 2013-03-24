from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maimaiti.views.home', name='home'),
    # url(r'^maimaiti/', include('maimaiti.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
