# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.db.models.fields import CharField, TextField, IntegerField
from django.conf import settings
from django.utils.functional import cached_property
import pusher
import requests
import twitter

from digifoot.lib.django.models import AbstractModel


log = logging.getLogger(__name__)


class SparkDeviceModel(AbstractModel):
    spark_id = CharField(unique=True, max_length=255)
    domain = TextField(blank=True)
    org_name = TextField(blank=True)
    goal_limit = IntegerField(default=10)
    TWITTER_CONSUMER_KEY = TextField(blank=True)
    TWITTER_CONSUMER_SECRET = TextField(blank=True)
    TWITTER_ACCESS_TOKEN_KEY = TextField(blank=True)
    TWITTER_ACCESS_TOKEN_SECRET = TextField(blank=True)
    SPARK_USERNAME = TextField(blank=True)
    SPARK_PASSWORD = TextField(blank=True)
    PUSHER_APP_ID = TextField(blank=True)
    PUSHER_PUBLIC = TextField(blank=True)
    PUSHER_PRIVATE = TextField(blank=True)
    PUSHER_CLUSTER = TextField(blank=True)

    def reset_state(self):
        try:
            result = requests.post('https://api.spark.io/oauth/token', {
                "username": self.SPARK_USERNAME,
                "password": self.SPARK_PASSWORD,
                "grant_type": "password"},
                                   auth=('spark', 'spark')
                                   )
            data = result.json()
            result = requests.post('https://api.particle.io/v1/devices/{0}/resetAll'.format(self.spark_id),
                                   {"access_token": data["access_token"]})
            return True
        except KeyError:
            return False

    @cached_property
    def pusher_client(self):
        return pusher.Pusher(
            app_id=self.PUSHER_APP_ID,
            key=self.PUSHER_PUBLIC,
            secret=self.PUSHER_PRIVATE,
            cluster=self.PUSHER_CLUSTER,
            ssl=True
        )

    @property
    def pusher_channel_name(self):
        return "goals-{0}".format(self.spark_id)

    def pusher_send_goal(self, white_goals, black_goals, finished):
        self.pusher_client.trigger(self.pusher_channel_name, 'goal', {
            'white_goals': white_goals,
            'black_goals': black_goals,
            'finished': finished,
        })

    @cached_property
    def twitter_api(self):
        account = {
            'consumer_key': self.TWITTER_CONSUMER_KEY,
            'consumer_secret': self.TWITTER_CONSUMER_SECRET,
            'access_token_key': self.TWITTER_ACCESS_TOKEN_KEY,
            'access_token_secret': self.TWITTER_ACCESS_TOKEN_SECRET,
        }

        return twitter.Api(**account)

    def __unicode__(self):
        return self.spark_id

