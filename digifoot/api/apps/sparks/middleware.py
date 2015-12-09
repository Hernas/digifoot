# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from digifoot.api.apps.sparks.models import SparkDeviceModel

log = logging.getLogger(__name__)

class SparkMiddleware(object):

    def process_request(self, request):
        request.spark = SparkDeviceModel.objects.last()