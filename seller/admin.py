from django.contrib import admin
from .models import Seller
# Register your models here.

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_filter = ('email','last_name','phoneNumber','gender')
    search_fields = ('email','last_name','phoneNumber','gender')
    list_display = (
        'first_name',
        'last_name',
        'email',
        'phoneNumber',
        'gender',
        'email'
    )