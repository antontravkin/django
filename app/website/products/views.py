from products.models import ProductCategory, Product, Basket
from users.models import User

from django.shortcuts import render, HttpResponseRedirect


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
