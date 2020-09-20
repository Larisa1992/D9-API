from django.contrib import admin
from django.urls import path, include
# from app.views import CategoryList, CategoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    # path('categories/', CategoryList.as_view(), name='category-detail'), # все категории
    # path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'), # единичная категория
]
