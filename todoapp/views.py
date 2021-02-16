from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404
from .models import Todo
from accounts.models import User
from todoapp.api.serializers import TodoListSerializer, TodoDetailSerializer, UserTodoListSerializer


class TodoList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        queryset = Todo.objects.all()
        serializer = TodoListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoDetailSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserTodoList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        objects = Todo.objects.filter(author=pk)
        serializer = UserTodoListSerializer(objects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)