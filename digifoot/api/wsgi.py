# -*- coding: utf-8 -*-
"""
WSGI config for digifootapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from __future__ import unicode_literals



import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digifoot.api.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None

application = Cling(get_wsgi_application())