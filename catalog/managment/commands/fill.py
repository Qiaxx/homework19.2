from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):
    help = 'Заполните базу данных данными из файла JSON.'

    @staticmethod
    def json_read_categories():
        # Здесь мы считываем данные из JSON файла с категориями
        with open('categories.json', 'r') as f:
            return json.load(f)

    @staticmethod
    def json_read_products():
        # Здесь мы считываем данные из JSON файла с продуктами
        with open('products.json', 'r') as f:
            return json.load(f)

    def handle(self, *args, **options):
        # Удалить все продукты
        Product.objects.all().delete()
        # Удалить все категории
        Category.objects.all().delete()

        # Создать список для хранения объектов категорий
        category_for_create = []

        # Обходим все значения категорий из JSON для создания объектов категорий
        for category_data in self.json_read_categories():
            category_for_create.append(
                Category(name=category_data['name'])
            )

        # Создаем объекты категорий в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Создать список для хранения объектов продуктов
        product_for_create = []

        # Обходим все значения продуктов из JSON для создания объектов продуктов
        for product_data in self.json_read_products():
            # Получаем категорию из базы данных для корректной связки объектов
            category = Category.objects.get(name=product_data['category'])
            product_for_create.append(
                Product(name=product_data['name'], category=category, price=product_data['price'])
            )

        # Создаем объекты продуктов в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
