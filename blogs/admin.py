from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content")
    list_filter = ("title",)
    search_fields = ("title", "content")
