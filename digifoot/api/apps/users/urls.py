# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from digifoot.api.apps.users.resources import MeResource, RegisterResource, RemindPassword, ChangePassword
from django.conf.urls import url

urlpatterns = [
    url(r'^me/$', MeResource.as_view()),
    url(r'^register/$', RegisterResource.as_view()),
    url(r'^remind/$', RemindPassword.as_view()),
    url(r'^change/$', ChangePassword.as_view()),
    url(r'^login/$', 'rest_framework_jwt.views.obtain_jwt_token'),
]