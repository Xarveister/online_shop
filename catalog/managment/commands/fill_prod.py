from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Функция очистки таблицы категории-Product БД и заполнение новыми данными"""
        Product.objects.all().delete()  # очистка таблицы Category

        new_product = [
            {'name_prod': 'Greenfield', 'description_prod': 'зеленый чай', 'img_prod': '', 'category_prod': 'Чай',
             'price_prod': '100'},
            {'name_prod': 'Помидоры', 'description_prod': 'красные томаты', 'img_prod': '', 'category_prod': 'Овощи',
             'price_prod': '50'},
            {'name_prod': 'Nescafe', 'description_prod': 'черный кофе', 'img_prod': '', 'category_prod': 'Кофе',
             'price_prod': '80'},
            {'name_prod': 'Степ', 'description_prod': 'шоколадные конфеты', 'img_prod': '', 'category_prod': 'Конфеты',
             'price_prod': '30'},
        ]

        product_list = []
        for item_data in new_product:
            product_list.append(Product(**item_data))

        Product.objects.bulk_create(product_list)  # заполняем БД
