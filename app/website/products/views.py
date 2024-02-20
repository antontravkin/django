from products.models import ProductCategory, Product
from django.shortcuts import render


def index(request):
    context = {
        "title": "Магазин одежды",
        "description": "Магазин одежды для вас",
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "Каталог",
        "description": "Каталог одежды для вас",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request, "products/products.html", context)
