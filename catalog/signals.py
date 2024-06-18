from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from catalog.models import Category
from catalog.services import get_cached_categories


@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def clear_category_cache(sender, **kwargs):
    cache.delete("categories")
    get_cached_categories()
