# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chats', '0002_chat_number_of_members'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='creator',
            new_name='author',
        ),
    ]