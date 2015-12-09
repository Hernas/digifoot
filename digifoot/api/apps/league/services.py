# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from digifoot.api.apps.users.serializers import UserModelSerializer

log = logging.getLogger(__name__)


def jwt_response_payload_handler(token, user=None, request=None):
    return UserModelSerializer(user).data