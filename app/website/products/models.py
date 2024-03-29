from tabnanny import verbose
from users.models import User
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    discription = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "патегорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    discription = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="product_images")
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"Продукт: {self.name} | Категория: {self.category.name}"


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = "корзина"
        verbose_name_plural = "корзина"

    def __str__(self) -> str:
        return f"Корзина для {self.user.username} | Продукт: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity
