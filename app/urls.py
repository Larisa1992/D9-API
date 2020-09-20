from app.views import PostList
from django.urls import path
from app.views import PostList, PostDetail


app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    # path('categories/', PostDetail.as_view(), name='post-detail'), # все категории
    # path('categories/<int:pk>', PostDetail.as_view(), name='post-detail'), # единичная категория
]