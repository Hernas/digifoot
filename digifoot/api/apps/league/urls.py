# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from digifoot.api.apps.league.views import StartMatchView, IndexView, PreviewMatchView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^new/(?P<players_num>2|4)/$', StartMatchView.as_view(), name="new"),
    url(r'^preview/$', PreviewMatchView.as_view(), name="preview"),
]