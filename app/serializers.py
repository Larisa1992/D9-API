from app.models import Post, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):    
    post_category = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name','post_category']


class CategoryDetailSerializer(serializers.ModelSerializer):    
    post_category = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'post_category']