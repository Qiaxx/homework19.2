# import json
# from django.core.management.base import BaseCommand
# from catalog.models import Category, Product
#
#
# class Command(BaseCommand):
#     help = "Fill the database with data from catalog.json"
#
#     def handle(self, *args, **options):
#         # Удаление всех существующих категорий и продуктов
#         Category.objects.all().delete()
#         Product.objects.all().delete()
#
#         # Чтение данных из JSON-файла
#         with open("catalog.json", "r") as file:
#             data = json.load(file)
#
#         # Создание категорий
#         for item in data:
#             if item["model"] == "catalog.category":
#                 category_fields = item["fields"]
#                 Category.objects.create(pk=item["pk"], **category_fields)
#
#         # Создание продуктов и связывание их с категориями
#         for item in data:
#             if item["model"] == "catalog.product":
#                 product_fields = item["fields"]
#                 product_fields["category"] = Category.objects.get(
#                     pk=product_fields["category"]
#                 )
#                 Product.objects.create(pk=item["pk"], **product_fields)
#
#         self.stdout.write(
#             self.style.SUCCESS(
#                 "Database successfully populated with data from catalog.json"
#             )
#         )
