from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf import settings
#from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^json_workbook/', 'pyxform_interface.views.json_workbook'),
    url(r'^$', 'pyxform_interface.views.index'),
    (r'^tmp/(?P<path>.*)$', 'pyxform_interface.views.serve_file'),
)

urlpatterns += staticfiles_urlpatterns()
