# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0003_auto_20151215_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='org_name',
            field=models.TextField(blank=True),
        ),
    ]
