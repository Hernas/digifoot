# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings

handler500 = 'digifoot.lib.resources.handler500'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('digifoot.api.apps.league.urls', namespace="league")),
    url(r'^users/', include('digifoot.api.apps.users.urls')),
    url(r'^sparks/', include('digifoot.api.apps.sparks.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
] + format_suffix_patterns([
])

# Debug
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )