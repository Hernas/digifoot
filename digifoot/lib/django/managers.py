# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import unicode_literals
from django.db import models
from model_utils.managers import PassThroughManagerMixin as Original_PassThroughManagerMixin



class PassThroughManagerMixin(Original_PassThroughManagerMixin):
    """
    A mixin that enables you to call custom QuerySet methods from your manager.
    """

    # pickling causes recursion errors
    _deny_methods = ['__getstate__', '__setstate__', '__getinitargs__',
                     '__getnewargs__', '__copy__', '__deepcopy__', '_db',
                     '__slots__', '__iter__']


class PassThroughManager(PassThroughManagerMixin, models.Manager):
    """
    just override ``model_utils.managers.PassThroughManager`` to include ``__iter__`` to
    ``_deny_methods``. thanks simon!
    """
    pass