from app.views import PostList
from django.urls import path
from app.views import PostList, PostDetail
from app.views import CategoryList, CategoryDetail, index

app_name = 'app'
urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='categories-list'), # все категории
    path('categories/<int:pk>', CategoryDetail.as_view(), name='categories-detail'), # единичная категория
]