# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Likes', '0002_remove_like_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='author',
        ),
    ]
