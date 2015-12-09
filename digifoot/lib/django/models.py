# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext, ugettext_lazy
from digifoot.lib.django import POSIX_ZERO
from digifoot.lib.django.managers import PassThroughManager
from digifoot.lib.django.querysets import ValidityQuerySet


class ModelMixins(object):
    def update(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
        self.save()
        return self

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        return True

    @classmethod
    def read(cls, pk):
        try:
            return cls.objects.get(id=pk)
        except cls.DoesNotExist:
            return None

    @classmethod
    def read_all(cls):
        try:
            return cls.objects.all()
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_model_and_app_name(cls):
        return '%s.%s' % (cls._meta.app_label, cls._meta.object_name)


class AbstractModel(ModelMixins, models.Model):
    class Meta:
        abstract = True
        ordering = ('created_at', 'pk')

    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=ugettext_lazy('Created at'))
    modified_at = models.DateTimeField(blank=True, auto_now=True, verbose_name=ugettext_lazy('Modified at'))
    deleted_at = models.DateTimeField(blank=False, default=POSIX_ZERO, verbose_name=ugettext_lazy('Deleted at'))

    objects = PassThroughManager.for_queryset_class(ValidityQuerySet)()
    admin_objects = models.Manager()

    def __unicode__(self):
        return u"[%s]" % (self.id,)