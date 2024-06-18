from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def get_cached_categories():
    """
    Получение списка категорий из кэша. В случае, если кэш пустой, берет данные из БД.
    """
    if not CACHE_ENABLED:
        return Category.objects.all()
    categories = cache.get("categories")
    if not categories:
        categories = Category.objects.all()
        cache.set("categories", categories, 60 * 15)  # Кэшируем на 15 минут
    return categories
