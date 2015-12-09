# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from decimal import Decimal

import logging
from django.db.models.fields import CharField, BooleanField, URLField, DecimalField
from django.db.models.fields.related import ForeignKey, ManyToManyField
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
    canceled = BooleanField(default=False)
    white_side_players = ManyToManyField(PlayerModel, related_name="white_side_players")
    black_side_players = ManyToManyField(PlayerModel, related_name="black_side_players")

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

        return match

    @classmethod
    def last_match(cls, spark):
        return cls.objects.filter(device=spark, finished=False).last()

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