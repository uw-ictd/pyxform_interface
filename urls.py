from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pyxform_interface.views.index'),

    (r'^tmp/(?P<path>.*)$', 'pyxform_interface.views.serve_xform'),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve'), {
        'document_root': ''
    },

#    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#        'document_root': settings.MEDIA_ROOT
#    }),
#
#    (r'^doc/(?P<path>.*)$', 'django.views.static.serve', {
#        'document_root': settings.DOC_ROOT
#    }),
)