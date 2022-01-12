from django.contrib import admin
from .models import Product, ProductGroup, ProductType

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'product_group',
        'product_type',
        'price',
        'rating',
        'brand',
        'image'
    )

    ordering = ('sku',)


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(ProductType, ProductTypeAdmin)