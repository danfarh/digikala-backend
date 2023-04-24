from django.contrib import admin

# Register your models here.
from .models import (
	Product,
    Color,
    Size,
    Image,
    Brand,
    ProductDiscount
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    list_display = (
        'title',
        'slug',
        'status'
    )

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = (
        'percent',
        'start',
        'end'
    )