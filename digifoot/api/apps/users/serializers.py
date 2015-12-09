# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, CharField
from rest_framework.serializers import ModelSerializer, Serializer
from digifoot.api.apps.users.models import User
from rest_framework_jwt import utils
from django.utils.translation import ugettext as _


class UserModelSerializer(ModelSerializer):
    token = SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'token')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            is_active=True
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def get_token(self, obj):
        payload = utils.jwt_payload_handler(obj)
        token = utils.jwt_encode_handler(payload)
        return token


class RemindPasswordParamsSerializer(Serializer):
    email = CharField()


class ChangePasswordParamsSerializer(Serializer):
    password = CharField()
    old_password = CharField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)

        super(ChangePasswordParamsSerializer, self).__init__(*args, **kwargs)
    def validate_old_password(self, value):
        """
        Check that old password is correct
        """
        if not self.user.check_password(value):
            raise ValidationError(_("Old password is not correct"))
        return value

