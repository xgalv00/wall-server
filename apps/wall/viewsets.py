from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from rest_framework import permissions
from common.utils import IsAuthorOrReadOnly


# class ArticleViewSet(viewsets.ModelViewSet):
#     """
#     List all articles, or create a new article.
#     """
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     lookup_field = 'slug'
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
#         else:
#             self.permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
#         return super().get_permissions()
#
#     @detail_route(methods=['post'])
#     # TODO test if could be assigned by non author
#     def assign_tag(self, request, pk=None):
#         article = self.get_object()
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             # TODO maybe rewrite save to look for instance first than update
#             tag = serializer.save()
#             article.tags.add(tag)
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     @detail_route(methods=['get'])
#     def list_article_tags(self, request, pk=None):
#         article = self.get_object()
#         tags = TagSerializer(data=article.tags.all(), many=True)
#         return Response({'tags': tags}, status=status.HTTP_200_OK)