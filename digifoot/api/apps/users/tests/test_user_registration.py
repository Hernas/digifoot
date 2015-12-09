# encoding: utf-8
from __future__ import absolute_import, unicode_literals
import json

import logging
from digifoot.api.apps.users.models import User
from digifoot.lib.tests.testcases import APITestCase, AuthenticatedAPITestCase
from rest_framework_jwt import utils

log = logging.getLogger(__name__)


class TestUserRegistration(APITestCase):
    def test_register(self):
        response = self.client.post('/users/register/', data={
            u'email': u'b@h.pl',
            u'password': u'a'
        }
        )

        user = User.objects.last()

        payload = utils.jwt_payload_handler(user)
        token = utils.jwt_encode_handler(payload)

        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(response.data, {
            u'email': u'b@h.pl',
            u'id': user.id,
            u'token': token
            })
        self.assertEqual(user.email, "b@h.pl")
        self.assertTrue(user.is_active)

    def test_email_uniq(self):
        response = self.client.post('/users/register/', data={
            u'email': u'b@h.pl',
            u'password': u'a'
        }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.last().email, "b@h.pl")

        response = self.client.post('/users/register/', data={
            u'email': u'b@h.pl',
            u'password': u'a'
        }
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {u'email': [u'This field must be unique.']})
        self.assertEqual(User.objects.last().email, "b@h.pl")