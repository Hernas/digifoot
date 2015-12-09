# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from digifoot.api.apps.league.models import MatchModel

from digifoot.api.apps.sparks.models import SparkDeviceModel
from digifoot.api.apps.sparks.serializers import SparkDeviceSerializer


log = logging.getLogger(__name__)


class SparksListResource(ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = SparkDeviceSerializer
    queryset = SparkDeviceModel.objects.all()



class GoalResource(RetrieveUpdateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = SparkDeviceSerializer
    queryset = SparkDeviceModel.objects.all()
    lookup_field = "spark_id"
    lookup_url_kwarg = "spark_id"

    def post(self, request, spark_id):

        instance = self.get_object()
        match = MatchModel.last_match(instance)
        if match is not None:
            return Response(data={"error": "Please start match first"}, status=HTTP_400_BAD_REQUEST)

        white = self.request.data['data'][0] == '1'


        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data=data)
