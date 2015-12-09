# encoding: utf-8
from __future__ import absolute_import, unicode_literals
import json

import logging
from django.core import mail
from mock import patch
from digifoot.api.apps.users.models import User
from digifoot.lib.tests.testcases import APITestCase, AuthenticatedAPITestCase
from rest_framework_jwt import utils

log = logging.getLogger(__name__)


class TestUserResource(AuthenticatedAPITestCase):
    def test_me(self):
        response = self.client.get('/users/me/')

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.data, {
            u'token': self.token,
            u'id': self.user.id,
            u'email': u'michal@hernas.pl'
            })

    def test_remind_password_fail(self):
        response = self.client.post('/users/remind/', data={"email": "asdasdasdasdasd@hernas.pl"})

        self.assertEqual(response.status_code, 404)

    def test_remind_password(self):
        old_hash = self.user2.password

        self.user2.refresh_from_db()
        self.assertNotEqual(old_hash, self.user2.password)

    def test_change_password(self):

        old_hash = self.user.password

        response = self.client.post('/users/change/', data={"old_password": "michal@hernas.pl",
                                                            "password": "b"})
        self.assertEqual(response.status_code, 200)

        self.user.refresh_from_db()
        self.assertNotEqual(old_hash, self.user.password)

    def test_change_password_fail(self):
        old_hash = self.user.password

        response = self.client.post('/users/change/', data={"old_password": "sasd",
                                                            "password": "b"})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'old_password': [u'Old password is not correct']})

        self.user.refresh_from_db()
        self.assertEqual(old_hash, self.user.password)