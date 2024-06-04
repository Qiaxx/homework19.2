from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    photo = models.ImageField(
        upload_to="users/photo/",
        verbose_name="фото",
        blank=True,
        null=True,
        help_text="Добавьте свое фото",
    )
    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="телефон",
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="страна",
        help_text="Добавьте свою страну",
    )

    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
