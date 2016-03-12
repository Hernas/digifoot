# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging
from django.views.decorators.cache import cache_page

from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView

from digifoot.api.apps.league.models import MatchModel
from digifoot.api.apps.league.serializers import MatchModelSerializer


log = logging.getLogger(__name__)


class MatchResource(RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = MatchModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        return MatchModel.objects.filter(device=self.request.spark, canceled=False).last()