from rest_framework import serializers

from todoapp.models import Project
from todoapp.models import Todo


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    contents = serializers.CharField(write_only=True)
    contents_type = serializers.CharField(write_only=True)
    class Meta:
        model = Todo
        fields = ('projects', 'author', 'title', 'contents', 'contents_type', 'id')


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('author', 'title', 'contents', 'contents_type', 'id', 'create_date', 'update_date', 'end_date', 'view')


class UserTodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'