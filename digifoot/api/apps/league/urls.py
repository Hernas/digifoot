# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from digifoot.api.apps.league.resources import MatchResource
from digifoot.api.apps.league.views import StartMatchView, IndexView, PreviewMatchView, CancelMatchView, \
    FinalResultsMatchView, ChangeSidesView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^new/(?P<players_num>2|4)/$', StartMatchView.as_view(), name="new"),
    url(r'^preview/$', PreviewMatchView.as_view(), name="preview"),
    url(r'^cancel/$', CancelMatchView.as_view(), name="cancel"),
    url(r'^final_results/$', FinalResultsMatchView.as_view(), name="final_results"),
    url(r'^change_sides/$', ChangeSidesView.as_view(), name="change_sides"),

    # API
    url(r'^matches/current/$', MatchResource.as_view(), name="current"),
]