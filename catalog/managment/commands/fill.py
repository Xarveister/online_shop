from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Функция очистки таблицы категории-Category БД и заполнение новыми данными"""
        Category.objects.all().delete()  # очистка таблицы Category

        # Добавить новые данные в базу данных
        new_category = [
            {'name_category': 'Чай', 'category_description': 'Бакалея'},
            {'name_category': 'Овощи', 'category_description': 'Свежие овощи'},

        ]

        category_list = []
        for item_data in new_category:
            category_list.append(Category(**item_data))

        Category.objects.bulk_create(category_list)  # заполняем таблицу
