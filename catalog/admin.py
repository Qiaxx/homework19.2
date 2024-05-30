from django.contrib import admin

from catalog.models import Category, Product, Version


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


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "version_name", "version_number")
    list_filter = ("product", "version_name", "version_number")
    search_fields = ("id", "product", "version_name")
