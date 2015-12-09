# encoding: utf-8
from __future__ import absolute_import, unicode_literals

import logging

from django.conf import settings
from django.test.testcases import TestCase
from rest_framework import test
from rest_framework_jwt import utils

from digifoot.api.apps.users.models import User


log = logging.getLogger(__name__)


class APIClient(test.APIClient):
    pass


class APITestCase(test.APITestCase):
    maxDiff = None
    client_class = APIClient

    def setUp(self):
        super(APITestCase, self).setUp()
        self.user1 = self.create_user('michal@hernas.pl', "Michał Hernas")
        self.user2 = self.create_user('bartosz@hernas.pl', 'Bartosz Hernas')

    def create_user(self, email, name):
        user = User.objects.create(
            name=name,
            email=email,
            is_active=True
        )
        user.set_password(email)
        user.save()
        return user

    def authenticate(self, user):
        """
        Authenticates the given user

        :param user: User to authenticate
        :type user: inventorum.ebay.apps.accounts.models.EbayUserModel
        """

        payload = utils.jwt_payload_handler(user)
        self.token = utils.jwt_encode_handler(payload)

        credentials = {
            'HTTP_AUTHORIZATION': 'JWT %s' % self.token
        }
        self.client.credentials(**credentials)

    def switch_to_user1(self):
        self.user = self.user1
        self.user.refresh_from_db()
        self.authenticate(self.user)

    def switch_to_user2(self):
        self.user = self.user2
        self.user.refresh_from_db()
        self.authenticate(self.user)


class AuthenticatedAPITestCase(APITestCase):
    def setUp(self):
        super(AuthenticatedAPITestCase, self).setUp()
        self.switch_to_user1()


class UnitTestCase(TestCase):
    pass
