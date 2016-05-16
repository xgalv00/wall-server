from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()

    class Meta:
        model = Token
        fields = ('key', 'user')
