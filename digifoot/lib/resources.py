# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.exceptions import APIException

class HttpException(APIException):
    status_code = 500

    def __init__(self, data=None, key=None):
        self.data = data
        self.key = key
        self.detail = {
            'message': data,
            'key': key
        }


class NotFound(HttpException):
    status_code = 404


class BadRequest(HttpException):
    status_code = 400

def handler500(request):
    """
    500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html')  # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))
