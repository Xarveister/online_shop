from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_prod', 'price_prod', 'category', 'is_published')
    search_fields = ('name_prod', 'description_prod', 'category')
    list_filter = ('category', )
    list_editable = ('is_published',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'name', 'is_active')
    list_display_links = ('number', 'name',)
    list_editable = ('is_active',)
