# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0009_oneononefightsubmission_expected_outcome'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanuser',
            name='description',
            field=models.TextField(blank='', default='', max_length=500),
        ),
    ]
