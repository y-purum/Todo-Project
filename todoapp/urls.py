from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path, include
from .views import TodoList, TodoDetail, UserTodoList


urlpatterns = [
    path('list/', TodoList.as_view()),
    path('list/detail/<int:pk>/', TodoDetail.as_view()),
    path('user/<int:pk>/', UserTodoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)