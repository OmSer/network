# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160929_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]