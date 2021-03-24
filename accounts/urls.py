from django.urls import path
from . import views

urlpatterns = [
    path('join/', views.create),
    path('login/', views.login),
]
