from django.contrib import admin
from . import models


@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('projects' ,'author',  'title', 'contents', 'contents_type', 'create_date', 'end_date')


@admin.register(models.Project)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'end_date')