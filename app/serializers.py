from app.models import Post, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False, read_only=True)
    # author_id = serializers.IntegerField(source='author')

    class Meta:
        model = Post
        fields = '__all__'
        # ['slug','title','status','content', 'updated','publication_date','category', 'author_id']

    # def create(self, validated_data):
    #     author = validated_data.pop('post_author')
    #     print(validated_data)
    #     # category = Category.objects.get(pk=validated_data.pop('event'))
    #     # instance = Post.objects.create(**validated_data)
    #     # Assignment.objects.create(Order=order, Equipment=instance)
    #     return instance

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