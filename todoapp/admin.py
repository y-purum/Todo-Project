from django.contrib import admin
from .models import Todo, Project


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('projects' ,'author',  'title', 'contents', 'contents_type', 'create_date', 'end_date')


@admin.register(Project)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_date', 'end_date')