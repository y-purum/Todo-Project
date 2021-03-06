from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include
from django.urls import path
from .views import ProjectList
from .views import ProjectDetail
from .views import TodoList
from .views import TodoDetail
from .views import UserTodoList


urlpatterns = [
    path('projects/', ProjectList.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('list/', TodoList.as_view()),
    path('list/<int:pk>/', TodoList.as_view()),
    path('detail/<int:pk>/', TodoDetail.as_view()),
    path('users/<int:pk>/', UserTodoList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)