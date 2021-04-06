from rest_framework import status
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

import os
from PIL import Image

import datetime
from glob import glob
from django.http import Http404
from accounts.models import User
from .models import Project
from .models import Todo
from todoapp.api.serializers import TodoListSerializer
from todoapp.api.serializers import TodoDetailSerializer
from todoapp.api.serializers import UserTodoListSerializer
from todoapp.api.serializers import ProjectListSerializer


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, foramt=None):
        objects = Project.objects.all()
        serializer = ProjectListSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProjectListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectListSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectListSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_200_OK)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoList(generics.ListCreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'contents']


class TodoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.view += 1
        serializer = TodoDetailSerializer(todo)

        if todo.view >= 999:
            return Response(serializer.data)

        todo.save()

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


class ImageResize():
    img_list = os.listdir('media/')

    for img_name in img_list:
        try: 
            img = Image.open('media/'+img_name)
            img_resize = img.resize((round(img.size[0]*0.5), round(img.size[1]*0.5)))
            img_resize.save('resize/'+img_name)
            img.close()
        except ValueError:
            print('Invalid image file')