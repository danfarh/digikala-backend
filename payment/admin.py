from django.contrib import admin
from .models import Payment
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ('payment','amount')
    search_fields = ('payment','amount')
    list_display = (
        'payment',
        'amount'
    )