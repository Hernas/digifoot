# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from django.db.models.fields import CharField
from django.conf import settings
import requests

from digifoot.lib.django.models import AbstractModel


log = logging.getLogger(__name__)


class SparkDeviceModel(AbstractModel):
    spark_id = CharField(unique=True, max_length=255)
    domain = TextField(blank=True)
    TWITTER_CONSUMER_KEY = TextField(blank=True)
    TWITTER_CONSUMER_SECRET = TextField(blank=True)
    TWITTER_ACCESS_TOKEN_KEY = TextField(blank=True)
    TWITTER_ACCESS_TOKEN_SECRET = TextField(blank=True)
    SPARK_USERNAME = TextField(blank=True)
    SPARK_PASSWORD = TextField(blank=True)

    def reset_state(self):
        try:
            result = requests.post('https://api.spark.io/oauth/token', {
                "username": settings.SPARK_ACCOUNT['username'],
                "password": settings.SPARK_ACCOUNT['password'],
                "grant_type": "password"},
                                   auth=(settings.SPARK_ACCOUNT['auth_user'], settings.SPARK_ACCOUNT['auth_password'])
                                   )
            data = result.json()
            result = requests.post('https://api.particle.io/v1/devices/{0}/resetAll'.format(self.spark_id),
                                   {"access_token": data["access_token"]})
            return True
        except KeyError:
            return False


    def __unicode__(self):
        return self.spark_id

