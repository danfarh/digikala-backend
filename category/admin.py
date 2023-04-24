from django.contrib import admin
from .models import Category
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('title','status')
    search_fields = ('title','status')
    list_display = (
        'title',
        'parent',
        'slug',
        'status'
    )
