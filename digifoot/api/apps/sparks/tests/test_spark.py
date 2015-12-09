# encoding: utf-8
from __future__ import absolute_import, unicode_literals
import json

import logging
from django.core import mail
from mock import patch
from digifoot.api.apps.league.models import PlayerModel, MatchModel
from digifoot.api.apps.sparks.models import SparkDeviceModel
from digifoot.api.apps.users.models import User
from digifoot.lib.tests.testcases import APITestCase, AuthenticatedAPITestCase
from rest_framework_jwt import utils

log = logging.getLogger(__name__)


class TestSparkResources(APITestCase):
    def test_goal(self):
        spark = SparkDeviceModel.objects.create(spark_id="123456")

        player1 = PlayerModel.objects.create(name="aaa'")
        player2 = PlayerModel.objects.create(name="bbb'")

        match = MatchModel.create_match(spark, player1, player2)
        self.assertTrue(match)
        self.assertTrue(spark)

        response = self.client.post('/sparks/{0}/goal/'.format(spark.spark_id), data={
            "data": "1,2",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(match.white_count, 1)
        self.assertEqual(match.black_count, 2)

        response = self.client.post('/sparks/{0}/goal/'.format(spark.spark_id), data={
            "data": "3,5",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(match.white_count, 3)
        self.assertEqual(match.black_count, 5)

    def test_match_finish(self):
        spark = SparkDeviceModel.objects.create(spark_id="123456")

        player1 = PlayerModel.objects.create(name="aaa'")
        player2 = PlayerModel.objects.create(name="bbb'")

        match = MatchModel.create_match(spark, player1, player2)
        self.assertTrue(match)
        self.assertTrue(spark)

        response = self.client.post('/sparks/{0}/goal/'.format(spark.spark_id), data={
            "data": "1,5",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(match.white_count, 1)
        self.assertEqual(match.black_count, 5)
        self.assertEqual(match.finished, False)

        response = self.client.post('/sparks/{0}/goal/'.format(spark.spark_id), data={
            "data": "1,6",
        })

        match.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(match.white_count, 1)
        self.assertEqual(match.black_count, 6)
        self.assertEqual(match.finished, True)