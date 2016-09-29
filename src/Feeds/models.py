from __future__ import unicode_literals

from django.db import models
from Profiles.models import User, ModelWithAuthor
from Core.models import ModelWithDate
from Entries.models import Post


class Feed(ModelWithAuthor):

    post = models.ForeignKey(Post)