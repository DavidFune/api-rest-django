from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=56, null=False)
    kg = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=56, null=False)
    description = models.CharField(max_length=256)

    def __str__(self):
            return self.name

class Recycle(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     category = models.ForeignKey(Category, on_delete=models.PROTECT)