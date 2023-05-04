from django.contrib import admin
from django.urls import path
from recycling.views import products
urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", products),
]
