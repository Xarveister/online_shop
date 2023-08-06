from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'price_prod', 'category_prod')
    list_filter = ('category_prod',)
    search_fields = ('name_prod', 'description_prod')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')
