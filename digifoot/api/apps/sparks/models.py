# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from decimal import Decimal

import logging
from django.db.models.fields import CharField, BooleanField, URLField, DecimalField
from digifoot.lib.django.models import AbstractModel


log = logging.getLogger(__name__)


class SparkDeviceModel(AbstractModel):
    spark_id = CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.spark_id