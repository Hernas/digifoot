# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser, Group
from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import ugettext, ugettext_lazy
from django_extensions.db.fields.json import JSONField
from digifoot.lib.django import POSIX_ZERO
from digifoot.lib.django.models import ModelMixins
from digifoot.lib.django.querysets import ValidityQuerySet

__author__ = 'bartg'


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        try:
            user = self.get_by_natural_key(email)
        except User.DoesNotExist:
            user = self.model(email=email)

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def user_post_save(sender, instance, created, **kwargs):
        """ This method is executed whenever an user object is saved
        """
        if created:
            pass
            # instance.groups.add(Group.objects.get(name='Staff'))
            # instance.save()

    def get_queryset(self):
        return ValidityQuerySet(self.model, using=self._db)

    def by_email(self, email):
        email = self.normalize_email(email)
        return self.get(email=email)



class User(AbstractBaseUser, PermissionsMixin, ModelMixins):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    email = models.EmailField(unique=True, verbose_name=ugettext_lazy("email"))
    name = models.CharField(null=True, default=None, max_length=255, verbose_name=ugettext_lazy("display name"))

    # Special fields
    created_at = models.DateTimeField(blank=True, auto_now_add=True, verbose_name=ugettext_lazy('Created at'))
    modified_at = models.DateTimeField(blank=True, auto_now=True,
                                       verbose_name=ugettext_lazy('Modified at'))
    is_staff = models.BooleanField(ugettext_lazy('staff status'), default=False,
                                   help_text=ugettext_lazy('Designates whether the user can log into this admin '
                                                           'site.'))
    is_active = models.BooleanField(ugettext_lazy('is active'), default=False)

    deleted_at = models.DateTimeField(blank=False, default=POSIX_ZERO, verbose_name=ugettext_lazy('Deleted at'))

    def get_short_name(self):
        return self.email

    @property
    def username(self):
        return self.get_short_name()