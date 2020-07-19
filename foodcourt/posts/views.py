from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import Post
from ..permissions import IsUserOrReadOnly
from .serializers import PostSerializer, CreatePostSerializer


class PostViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsUserOrReadOnly,)


class PostCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (AllowAny,)