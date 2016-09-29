from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from Core.models import ModelWithDate
from Likes.models import LikeMixin
from Profiles.models import User, ModelWithAuthor


class Post(ModelWithDate, LikeMixin, ModelWithAuthor):

    title = models.CharField(max_length=256, blank=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    number_of_comments = models.PositiveIntegerField(default=0)


class Comment(ModelWithDate, LikeMixin, ModelWithAuthor):

    post = models.ForeignKey(Post)
    text = models.CharField(max_length=1024)


@receiver(post_save, sender = Comment)
def comment_post_save(instance, created=False, **kwargs):
    if created:
        post_object = instance.post
        post_object.number_of_comments += 1
        post_object.save()