from django.conf import settings
from rest_framework import serializers
from PhotoSharingApplication.models import Pictures, Categories, UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name', 'image')


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pictures
        fields = ('id', 'name', 'image', 'likes_count')
