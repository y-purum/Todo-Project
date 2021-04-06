from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = format_suffix_patterns([
    path('', views.ProjectList.as_view()),
    path('<int:pk>/', views.ProjectDetail.as_view()),
    path('list/', views.TodoList.as_view()),
    path('list/<int:pk>/', views.TodoList.as_view()),
    path('list/detail/<int:pk>/', views.TodoDetail.as_view()),
    path('users/<int:pk>/', views.UserTodoList.as_view()),
]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)