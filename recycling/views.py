from rest_framework import viewsets, generics
from recycling.models import Product, Category, Recycle
from recycling.serializer import ProductSerializer, CategorySerializer, RecycleSerializer, ListProductsByCategotySerializer
class ProductViewSet(viewsets.ModelViewSet):
    """Show all Products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class CategoryViewSet(viewsets.ModelViewSet):
    """Show all Categories"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecycleViewSet(viewsets.ModelViewSet):
    """Show all Recycle"""
    queryset = Recycle.objects.all()
    serializer_class = RecycleSerializer

class ListProductsByCategoty(generics.ListAPIView):
    """Show all Products by Category"""
    def get_queryset(self):
        queryset = Recycle.objects.filter(category_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListProductsByCategotySerializer
     