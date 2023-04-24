from django.contrib import admin
from .models import (Order,Invoice)
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('state','amount')
    search_fields = ('state','amount')
    list_display = (
        'state',
        'amount',
        'deliverMethod',
        'paymentMethod',
        'create',
        'update'
    )

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass  

