# encoding: utf-8
from __future__ import absolute_import, unicode_literals
import logging

log = logging.getLogger(__name__)

class ErrorHandlingMiddleware(object):

    def process_exception(self, request, exception):
        log.warn(exception)