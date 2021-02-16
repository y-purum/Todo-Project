from rest_framework import permissions
from rest_framework import viewsets

from .models import Comment
from comments.api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)