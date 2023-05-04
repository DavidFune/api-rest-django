from rest_framework import serializers
from recycling.models import Product, Category, Recycle

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RecycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recycle
        fields = '__all__'