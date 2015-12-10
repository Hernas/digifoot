# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer

from digifoot.api.apps.league.models import MatchModel


class MatchModelSerializer(ModelSerializer):
    class Meta:
        model = MatchModel
        fields = ('id', 'white_count', 'black_count')
        read_only_fields = fields
