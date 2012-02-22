from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'xlsform.views.index'),

    (r'^tmp/(?P<path>.*)$', 'views.serve_xform'),

    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.CSS_ROOT
    }),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

    (r'^doc/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.DOC_ROOT
    }),
)
