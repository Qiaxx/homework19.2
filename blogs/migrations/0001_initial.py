# Generated by Django 5.0.6 on 2024-05-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                (
                    "content",
                    models.TextField(help_text="Введите текст", verbose_name="Текст"),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Вставьте изображение",
                        null=True,
                        upload_to="blog_previews",
                        verbose_name="Изображение",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "published",
                    models.BooleanField(default=False, verbose_name="Опубликовано"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="Введите количество просмотров",
                        null=True,
                        verbose_name="Количество просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья блога",
                "verbose_name_plural": "Статьи блога",
            },
        ),
    ]
