from rest_framework import viewsets
from rest_framework import permissions

from common.utils import IsAuthorOrReadOnly
from wall.models import Post
from wall.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    List all articles, or create a new article.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
        else:
            self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
        return super().get_permissions()