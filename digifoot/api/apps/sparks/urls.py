# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from digifoot.api.apps.sparks.resources import SparksListResource, GoalResource


urlpatterns = [
    url(r'^$', SparksListResource.as_view(), name='list'),
    url(r'^(?P<spark_id>[0-9A-Za-z]+)/goal/$', GoalResource.as_view(), name='alarm'),
]