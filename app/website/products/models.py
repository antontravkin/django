from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    discription = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=128)
    discription = models.TextField(null=True, blank=True)
    price = models. DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
