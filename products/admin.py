from django.contrib import admin
from .models import Product, Category, Sub_category


class ProductAdmin(admin.ModelAdmin):
    """
    Class extends djangos ModelAdmin class
    """
    list_display = (
        'sku',
        'name',
        'category',
        'sub_category',
        'manufacturer',
        'price',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Class extends djangos ModelAdmin class
    """
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('friendly_name',)


class SubCategoryAdmin(admin.ModelAdmin):
    """
    Class extends djangos ModelAdmin class
    """
    list_display = (
        'friendly_name',
        'name',
        'category',
    )
    ordering = ('category', 'friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_category, SubCategoryAdmin)
