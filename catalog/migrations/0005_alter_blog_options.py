# Generated by Django 5.0.6 on 2024-05-15 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_alter_blog_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "verbose_name": "Статья блога",
                "verbose_name_plural": "Статьи блога",
            },
        ),
    ]
