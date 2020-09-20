from app.models import Post, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):    
    # posts = PostSerializer(many=True)
    posts_category = PostSerializer(many=True)
    class Meta:
        model = Category
        fields = ['slug','name','posts_category']