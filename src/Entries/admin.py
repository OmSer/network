from django.contrib import admin
from .models import *


class ListAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time',)

models = [Post, Comment]
admin.site.register(models, ListAdmin)