import slugify

from rest_framework import serializers
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from wall.models import Post


# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     author = serializers.CharField(source='author.get_full_name', read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ('name', 'author', 'image', 'text', 'url')
#         extra_kwargs = {
#             'url': {'lookup_field': 'slug'}
#         }
#
#     def create(self, validated_data):
#         validated_data['slug'] = slugify.slugify(validated_data['name']).lower()
#         return super().create(validated_data)
#
#     def validate_name(self, value):
#         """
#         Check that the name is unique if slugified.
#         """
#         slug = slugify.slugify(value).lower()
#         if Article.objects.filter(Q(name__exact=value) | Q(slug__iexact=slug)):
#             raise serializers.ValidationError(_("Name should be unique"))
#         return value

