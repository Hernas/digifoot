# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.db.models.fields import CharField, BooleanField, DateTimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils import timezone
import twitter
from django.conf import settings

from digifoot.api.apps.sparks.models import SparkDeviceModel
from digifoot.lib.django.models import AbstractModel


log = logging.getLogger(__name__)


class PlayerModel(AbstractModel):
    name = CharField(unique=True, max_length=255, null=False, blank=False)


class MatchModel(AbstractModel):
    class WrongPlayers(Exception):
        pass

    class MatchAlreadyInProgress(Exception):
        pass

    device = ForeignKey(SparkDeviceModel, related_name="matches")
    finished = BooleanField(default=False)
    finished_at = DateTimeField(blank=False, default=timezone.now)

    tweeted = BooleanField(default=False)
    canceled = BooleanField(default=False)

    white_side_players = ManyToManyField(PlayerModel, related_name="white_side_players")
    black_side_players = ManyToManyField(PlayerModel, related_name="black_side_players")

    @property
    def duration(self):
        return self.finished_at - self.created_at

    def cancel(self):
        self.canceled = True
        self.save()

    def finish(self):
        self.finished = True
        self.finished_at = timezone.now()
        self.save()

        self.tweet_if_needed()

    @property
    def team_names(self):
        if self.white_count > self.black_count:
            winners = self.white_side_players
            losers = self.black_side_players
        else:
            winners = self.black_side_players
            losers = self.white_side_players

        winners_names = [winner.name for winner in winners.all()]
        losers_names = [loser.name for loser in losers.all()]
        return winners_names, losers_names

    @property
    def final_scores(self):
        if self.white_count > self.black_count:
            winners = self.white_count
            losers = self.black_count
        else:
            winners = self.black_count
            losers = self.white_count

        return winners, losers

    @property
    def tweet_message(self):

        winners, losers = self.team_names

        easter_egg = set(winners + losers) == set(["mfts", "strobl", "bartoszhernas", "michal.hernas"])

        winners = " ".join(["@{0}".format(w) for w in winners])
        losers = " ".join(["@{0}".format(l) for l in losers])

        winners_score, losers_score = self.final_scores

        status = "Schönes Ding: {winners} gewinnt {winners_score}:{losers_score} gegen {losers}".format(
            winners=winners,
            winners_score=winners_score,
            losers_score=losers_score,
            losers=losers,
        )

        if easter_egg:
            status = "Piękna rzecz: {winners} wygrali {winners_score}:{losers_score} z {losers} #hernas #hackevents".format(
                winners=winners,
                winners_score=winners_score,
                losers_score=losers_score,
                losers=losers,
            )

        return status

    def tweet_if_needed(self):
        if not self.tweeted:
            account = settings.TWITTER_ACCOUNT
            api = twitter.Api(**account)

            result = api.PostUpdate(self.tweet_message)

            self.tweeted = True
            self.save()


    @classmethod
    def create_match(cls, spark, white_player1, black_player1, white_player2=None, black_player2=None):
        if cls.last_match(spark) is not None:
            raise cls.MatchAlreadyInProgress()

        if white_player1 is None or black_player1 is None:
            raise cls.WrongPlayers()

        match = MatchModel()
        match.device = spark
        match.save()

        match.white_side_players.add(white_player1)
        match.black_side_players.add(black_player1)

        if white_player2:
            match.white_side_players.add(white_player2.pk)
        if black_player2:
            match.black_side_players.add(black_player2)

        match.device.reset_state()
        return match

    @classmethod
    def last_match(cls, spark):
        return cls.objects.filter(device=spark, finished=False, canceled=False).last()

    @property
    def white_count(self):
        return self.goals.filter(whites=True).count()

    @property
    def black_count(self):
        return self.goals.filter(whites=False).count()


class GoalModel(AbstractModel):
    match = ForeignKey(MatchModel, related_name="goals")
    whites = BooleanField()

    @classmethod
    def do_score(cls, spark, whites):
        goal = GoalModel()
        goal.match = MatchModel.last_match(spark)
        goal.whites = whites
        goal.save()
        return goal