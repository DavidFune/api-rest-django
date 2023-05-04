from django.contrib import admin
from recycling.models import Product, Category, Recycle

class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'kg','description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Product, Products)

class Categories(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    
admin.site.register(Category, Categories)


class Recycling(admin.ModelAdmin):
    list_display = ('id', 'product', 'category')
    list_display_links = ('id',)
    
admin.site.register(Recycle, Recycling)