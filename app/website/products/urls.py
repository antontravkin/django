from products.views import products, basket_add
from django.urls import path


app_name = "products"

urlpatterns = [
    path("", products, name="index"),
    path("baskets/add/<int:product_id>/", basket_add, name="basket_add"),
]
