from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cost_product", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")
