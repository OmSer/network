# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0003_auto_20160927_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default=None, max_length=32),
        ),
    ]