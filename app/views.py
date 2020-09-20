from django.shortcuts import render
from app.models import Post, Category
from app.serializers import PostSerializer,  CategorySerializer, CategoryDetailSerializer
from rest_framework import generics  


# ListCreateAPIView может обрабатывать Get и Post (создавать экземпляры класса) запросы
# ListAPIView может обрабатывать только Get запросы
# app/posts GET, POST

class PostList(generics.ListCreateAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

# app/posts/<pk> GET, POST, PATCH, DELETE
class PostDetail(generics.RetrieveUpdateDestroyAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

# categories/ GET, POST
class CategoryList(generics.ListCreateAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer

# categories/<pk> GET, POST, PATCH, DELETE
class CategoryDetail(generics.ListCreateAPIView):  
     queryset = Category.objects.all()  
     serializer_class = CategoryDetailSerializer