from django.db import models

from blog.models import NULLABLE
from config import settings


class Product(models.Model):
    name_prod = models.CharField(max_length=100, verbose_name='Наименование')
    description_prod = models.CharField(max_length=100, verbose_name='Описание')
    img_prod = models.ImageField(upload_to='preview', verbose_name='Превью', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    price_prod = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True,
                                             help_text='Введите цену продукта в рублях')
    data_create_prod = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    data_change_prod = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', **NULLABLE)

    def __str__(self):
        return f'{self.name_prod} {self.category} {self.price_prod} {self.description_prod}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Наименование категории')
    category_description = models.CharField(max_length=100, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category} {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.CharField(max_length=10, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='имя версии')
    is_active = models.BooleanField(default=True, verbose_name='текущая версия')

    def __str__(self):
        return f'{self.name} ({self.number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
