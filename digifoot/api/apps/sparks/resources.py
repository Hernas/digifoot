# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import logging

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from digifoot.api.apps.league.models import MatchModel, GoalModel

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
        goal_limit = instance.goal_limit

        match = MatchModel.last_match(instance)
        if match is None:
            return Response(data={"error": "Please start match first"})

        white, black = self.request.data['data'].split(',')
        try:
            white = int(white)
            black = int(black)
        except ValueError:
            return Response(data={"error": "Wrong data. Data needs to be two numeric values separated by comma"})

        white = min(white, goal_limit)
        black = min(black, goal_limit)

        for index in range(match.white_count, white):
            GoalModel.objects.create(whites=True, match=match)

        for index in range(match.black_count, black):
            GoalModel.objects.create(whites=False, match=match)


        if white >= goal_limit or black >= goal_limit:
            match.finish()

        match.send_to_pusher()
        return Response({})
