from django.utils.archive import extract
from users.models import User
from django.contrib import admin

from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)
    inlines = (BasketAdmin,)
