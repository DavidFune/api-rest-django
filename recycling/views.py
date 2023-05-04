from rest_framework import viewsets
from recycling.models import Product, Category
from recycling.serializer import ProductSerializer, CategorySerializer
class ProductViewSet(viewsets.ModelViewSet):
    """Show all Products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    """Show all Categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer