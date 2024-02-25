from products.models import ProductCategory, Product, Basket

from django.contrib import admin

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "category")
    fields = ("name", "discription", ("price", "quantity"), "image", "category")
    search_fields = ("name",)
    ordering = ("price",)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = (
        "product",
        "quantity",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0
