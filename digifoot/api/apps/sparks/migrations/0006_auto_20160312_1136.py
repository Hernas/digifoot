# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-12 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0005_sparkdevicemodel_goal_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='PUSHER_PRIVATE',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='PUSHER_PUBLIC',
            field=models.TextField(blank=True),
        ),
    ]
