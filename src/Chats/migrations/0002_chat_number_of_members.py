# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='number_of_members',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
