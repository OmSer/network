#coding: utf-8

from __future__ import unicode_literals

from django.db import models
from Core.models import ModelWithDate


class User(ModelWithDate):

    first_name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.second_name

    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователи"


class ModelWithAuthor(models.Model):

    author = models.ForeignKey(User)

    class Meta:
        abstract = True


class Friendship(ModelWithDate):

    initiator = models.ForeignKey(User, related_name="initiator")
    accepter = models.ForeignKey(User, related_name="accepter")


class Group(ModelWithDate):

    name = models.CharField(max_length=64)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name='creator')
    members = models.ManyToManyField(User, through='Membership')
    number_of_members = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Membership(ModelWithDate):

    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.user.second_name + ' ' + self.user.first_name + '--' + self.group.name
