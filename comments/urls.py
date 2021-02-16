from rest_framework.routers import DefaultRouter

from django.urls import path, include
from .views import CommentViewSet


router = DefaultRouter()
router.register(r'detail', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]