# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparks', '0002_auto_20151209_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='SPARK_PASSWORD',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='SPARK_USERNAME',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='TWITTER_ACCESS_TOKEN_KEY',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='TWITTER_ACCESS_TOKEN_SECRET',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='TWITTER_CONSUMER_KEY',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='TWITTER_CONSUMER_SECRET',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='sparkdevicemodel',
            name='domain',
            field=models.TextField(blank=True),
        ),
    ]
