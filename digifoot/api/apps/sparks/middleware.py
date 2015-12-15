# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from digifoot.api.apps.sparks.models import SparkDeviceModel

log = logging.getLogger(__name__)

class SparkMiddleware(object):

    def process_request(self, request):
        domain = request.META.get('HTTP_HOST', "")
        log.info("Using spark for domain: %s", domain)
        spark = SparkDeviceModel.objects.filter(domain=domain).last()
        if not spark:
            spark = SparkDeviceModel.objects.first()

        request.spark = spark