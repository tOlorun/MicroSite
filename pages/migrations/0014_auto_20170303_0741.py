# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20170303_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]