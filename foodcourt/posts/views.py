from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from ..permissions import IsUserOrReadOnly
from .models import Post
from .serializers import CreatePostSerializer, PostSerializer


class PostViewSet(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Updates and retrieves user accounts
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsUserOrReadOnly,)


class PostCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates user accounts
    """

    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = (AllowAny,)
