from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = '�������� ������ ���������� � ������������ �������'

    def handle(self, *args, **kwargs):
        # ������� ������ ����������
        moderators_group, created = Group.objects.get_or_create(name='moderator')

        # �������� �����
        content_type = ContentType.objects.get_for_model(Product)
        cancel_publish_product = Permission.objects.get(
            codename='cancel_publish_product',
            content_type=content_type,
        )
        change_product_description_permission = Permission.objects.get(
            codename='change_product_description',
            content_type=content_type,
        )
        change_category_product_permission = Permission.objects.get(
            codename='change_category_product',
            content_type=content_type,
        )

        # ��������� ����� ������
        moderators_group.permissions.add(cancel_publish_product, change_product_description_permission, change_category_product_permission)

        self.stdout.write(self.style.SUCCESS('������ ���������� ������� � ����� ���������.'))