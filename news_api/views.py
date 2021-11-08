from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
