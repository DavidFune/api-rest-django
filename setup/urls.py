from django.contrib import admin
from django.urls import path, include
from recycling.views import ProductViewSet, CategoryViewSet, RecycleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='Products')
router.register('categories', CategoryViewSet, basename='Categories')
router.register('recycling', RecycleViewSet, basename='Recycling')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
