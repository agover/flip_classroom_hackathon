# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181015_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatevideopage',
            name='playing_views',
            field=models.IntegerField(default=0),
        ),
    ]
