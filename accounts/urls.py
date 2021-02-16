from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('login/', views.login),
]