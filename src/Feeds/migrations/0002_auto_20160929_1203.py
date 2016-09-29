# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0005_auto_20160927_2022'),
        ('Feeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='owner',
        ),
        migrations.AddField(
            model_name='feed',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Profiles.User'),
            preserve_default=False,
        ),
    ]
