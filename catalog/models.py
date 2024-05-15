from django.db import models
from django.urls import reverse


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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", help_text="Введите заголовок"
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField(verbose_name="Текст", help_text="Введите текст")
    preview = models.ImageField(
        upload_to="catalog/blog_previews",
        verbose_name="Изображение",
        help_text="Вставьте изображение",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
