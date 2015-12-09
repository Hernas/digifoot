# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
from rest_framework import status, permissions
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from digifoot.api.apps.users.models import User
from digifoot.api.apps.users.serializers import UserModelSerializer, RemindPasswordParamsSerializer, \
    ChangePasswordParamsSerializer
from django.utils.translation import ugettext as _
from django.conf import settings


log = logging.getLogger(__name__)


class MeResource(GenericAPIView):
    serializer_class = UserModelSerializer

    def get(self, request):
        serializer = self.get_serializer(instance=request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class RegisterResource(GenericAPIView):
    serializer_class = UserModelSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemindPassword(GenericAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        serializer = RemindPasswordParamsSerializer(data=request.DATA)
        serializer.is_valid(raise_exception=True)

        try:
            user = User.objects.by_email(serializer.data['email'])
        except User.DoesNotExist:
            raise NotFound()

        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        mail.send(
            [user.email],
            settings.SERVER_EMAIL,
            subject=_('Password reminder'),
            message=_('New password: {0}').format(new_password),
            html_message=_('New password: {0}').format(new_password),
            priority='now',
        )

        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

class ChangePassword(GenericAPIView):

    def post(self, request):
        serializer = ChangePasswordParamsSerializer(data=request.DATA, user=self.request.user)
        serializer.is_valid(raise_exception=True)

        new_password = serializer.data['password']
        self.request.user.set_password(new_password)
        self.request.user.save()

        mail.send(
            [self.request.user.email],
            settings.SERVER_EMAIL,
            subject=_('Password has been changed'),
            message=_('Password has been changed for your account'),
            html_message=_('Password has been changed for your account'),
            priority='now',
        )

        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
