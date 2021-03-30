from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProjectList.as_view()),
    path('<int:pk>/', views.ProjectDetail.as_view()),
    path('list/', views.TodoList.as_view()),
    path('list/<int:pk>/', views.TodoList.as_view()),
    path('list/detail/<int:pk>/', views.TodoDetail.as_view()),
    path('users/<int:pk>/', views.UserTodoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)