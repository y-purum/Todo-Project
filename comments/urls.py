from rest_framework.routers import DefaultRouter

from django.urls import include
from django.urls import path

from . import views


router = DefaultRouter()
router.register(r'detail', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]