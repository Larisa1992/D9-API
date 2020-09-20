from django.shortcuts import render
from app.models import Post,   Category
from app.serializers import PostSerializer,  CategorySerializer
from rest_framework import generics  


# ListCreateAPIView может обрабатывать Get и Post (создавать экземпляры класса) запросы
# ListAPIView может обрабатывать только Get запросы
class PostList(generics.ListCreateAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveAPIView):  
#     queryset = Category.objects.all()  
#     serializer_class = CategorySerializer