from django.contrib import admin
from .models import *


class ListAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time',)

models = [User, Friendship, Group, Membership]
admin.site.register(models, ListAdmin)