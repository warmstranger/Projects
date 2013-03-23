from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tree/home','tree.views.home'),
    url(r'^tree/create_node$','tree.views.create_node'),
    url(r'^tree/show_tree$','tree.views.show_tree'),
    url(r'^tree/show_tree/(.+)/$','tree.views.show_projecttree'),
    url(r'^tree/create_node_type/(.+)/(.+)/$','tree.views.create_node_type'),
    url(r'^tree/save_tree$','tree.views.save_tree'),
    url(r'^tree/download_file/(.+)/$','tree.views.download_file'),
    url(r'^tree/add_node$','tree.views.add_node'),
    url(r'^tree/delete_node/(.+)/$','tree.views.delete_node'),
)