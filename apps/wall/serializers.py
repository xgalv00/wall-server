from rest_framework import serializers

from wall.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'image', 'description', 'url')

