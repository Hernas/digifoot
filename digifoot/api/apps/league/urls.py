# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from django.views.decorators.cache import cache_page

from digifoot.api.apps.league.resources import MatchResource
from digifoot.api.apps.league.views import StartMatchView, IndexView, PreviewMatchView, CancelMatchView, \
    FinalResultsMatchView, ChangeSidesView, QuickStartView, CreditsView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^new/(?P<players_num>2|4)/$', StartMatchView.as_view(), name="new"),
    url(r'^preview/$', PreviewMatchView.as_view(), name="preview"),
    url(r'^cancel/$', CancelMatchView.as_view(), name="cancel"),
    url(r'^final_results/$', FinalResultsMatchView.as_view(), name="final_results"),
    url(r'^change_sides/$', ChangeSidesView.as_view(), name="change_sides"),
    url(r'^quick_start/$', QuickStartView.as_view(), name="quick_start"),
    url(r'^credits/$', CreditsView.as_view(), name="credits"),

    # API
    url(r'^matches/current/$', cache_page(2)(MatchResource.as_view()), name="current"),
]