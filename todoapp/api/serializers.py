from rest_framework import serializers
from todoapp.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    contents = serializers.CharField(write_only=True)
    contents_type = serializers.CharField(write_only=True)
    class Meta:
        model = Todo
        fields = ('author', 'title', 'contents', 'contents_type', 'id')


class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('author', 'title', 'contents', 'contents_type', 'id', 'create_date', 'update_date')


class UserTodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'