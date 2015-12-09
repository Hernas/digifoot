# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
import logging

from django.db.models import Manager
from django.db.models.query import QuerySet
from django.contrib.auth.models import UserManager
from django.db.models.query_utils import Q
from digifoot.lib.django import POSIX_ZERO


log = logging.getLogger(__name__)


class ValidityQuerySet(QuerySet):
    def __init__(self, *args, **kwargs):
        super(ValidityQuerySet, self).__init__(*args, **kwargs)
        self.query.add_q(Q(deleted_at=POSIX_ZERO))

    def delete(self):
        return super(ValidityQuerySet, self).update(deleted_at=timezone.now())


class ValidityManager(Manager):
    def get_queryset(self):
        return ValidityQuerySet(self.model, using=self._db)


class ValidityUserManager(UserManager, ValidityManager):
    pass
