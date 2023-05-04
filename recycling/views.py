from rest_framework import viewsets
from recycling.models import Product, Category, Recycle
from recycling.serializer import ProductSerializer, CategorySerializer, RecycleSerializer
class ProductViewSet(viewsets.ModelViewSet):
    """Show all Products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    """Show all Categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecycleViewSet(viewsets.ModelViewSet):
    """Show all Categories"""
    queryset = Recycle.objects.all()
    serializer_class = RecycleSerializer