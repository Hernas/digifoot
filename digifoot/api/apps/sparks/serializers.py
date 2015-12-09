# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.serializers import ModelSerializer
from digifoot.api.apps.sparks.models import SparkDeviceModel


class SparkDeviceSerializer(ModelSerializer):
    class Meta:
        model = SparkDeviceModel
        fields = (
            'spark_id',
        )


