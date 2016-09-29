from __future__ import unicode_literals

from django.db import models
from Profiles.models import User, ModelWithAuthor
from Core.models import ModelWithDate

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


class Like(ModelWithDate, ModelWithAuthor):

    item_type = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')


class LikeMixin(models.Model):

    likes = GenericRelation(Like, content_type_field='item_type', object_id_field ='item_id')

    class Meta:
        abstract =True