# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateView
from digifoot.api.apps.league.forms import StartMatchForm
from digifoot.api.apps.league.models import MatchModel, PlayerModel

log = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "index.html"


class StartMatchView(TemplateView):
    template_name = "startmatch.html"

    def get(self, request, players_num, *args, **kwargs):
        if MatchModel.last_match(request.spark):
            return redirect(reverse('league:preview'))

        return self.render_to_response({"form": StartMatchForm(), "four_players": players_num == '4'})

    def post(self, request, *args, **kwargs):
        form = StartMatchForm(self.request.POST)
        if form.is_valid():
            player1_white, _ = PlayerModel.objects.get_or_create(name=form.cleaned_data['player1_white'])
            player2_white = form.cleaned_data['player2_white']

            player1_black, _ = PlayerModel.objects.get_or_create(name=form.cleaned_data['player1_black'])
            player2_black = form.cleaned_data['player2_black']

            if player2_black:
                player2_black, _ = PlayerModel.objects.get_or_create(name=player2_black)
            else:
                player2_black = None

            if player2_white:
                player2_white, _ = PlayerModel.objects.get_or_create(name=player2_white)
            else:
                player2_white = None

            try:
                match = MatchModel.create_match(request.spark, player1_white, player1_black, player2_white,
                                                player2_black)
                return redirect(reverse('league:preview'))

            except MatchModel.WrongPlayers:
                error = "You need minimum two players, one for each team."
            except MatchModel.MatchAlreadyInProgress:
                error = "Match is already in progress"

        return self.render_to_response({"form": form})


class PreviewMatchView(TemplateView):
    template_name = "preview.html"

    def get(self, request, *args, **kwargs):
        if not MatchModel.last_match(request.spark):
            return redirect(reverse('league:new'))

        return self.render_to_response({})