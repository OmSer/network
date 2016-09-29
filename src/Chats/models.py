from __future__ import unicode_literals

from django.db import models
from Profiles.models import User, ModelWithAuthor
from Core.models import ModelWithDate


class Message(ModelWithDate):

    theme = models.CharField(max_length=64)
    text = models.TextField()
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')


class Chat(ModelWithDate, ModelWithAuthor):

    number_of_members = models.PositiveIntegerField(default=0)