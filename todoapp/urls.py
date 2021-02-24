from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path, include
from .views import TodoList, TodoDetail, UserTodoList
# from .views import Search

urlpatterns = [
    path('list/', TodoList.as_view()),
    path('list/<int:pk>/', TodoList.as_view()),
    path('detail/<int:pk>/', TodoDetail.as_view()),
    path('user/<int:pk>/', UserTodoList.as_view()),
    # path('search/', Search_as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)