from django.contrib import admin
from .models import Discount
# Register your models here.
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_filter = ('code','percent','active','condition')
    search_fields = ('code','percent','active','condition')
    list_display = (
        'reason',
        'condition',
        'code',
        'percent',
        'active'
    )