from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите категорию"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Товар", help_text="Введите название товара"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание товара",
        help_text="Введите описание товара",
    )
    image_product = models.ImageField(
        upload_to="catalog/media",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        blank=True,
        null=True,
        related_name="catalog",
    )
    cost_product = models.IntegerField(
        verbose_name="Стоимость товара", help_text="Введите стоимость товара"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", help_text="Укажите владельца товара", blank=True, null=True, on_delete=models.SET_NULL)
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        permissions = [
            ("can_cancel_publish_product", "Can Cancel Publish Product"),
            ("can_change_description_product", "Can Change Description Product"),
            ("can_change_category_product", "Can Change Category Product"),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.CASCADE,
        verbose_name="Товар",
    )
    version_number = models.CharField(
        max_length=50, verbose_name="Номер версии", help_text="Введите номер версии"
    )
    version_name = models.CharField(
        max_length=255,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    is_current = models.BooleanField(default=False, verbose_name="Активная версия")

    class Meta:
        verbose_name = "Версия товара"
        verbose_name_plural = "Версии товара"

    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"
