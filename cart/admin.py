from django.contrib import admin
from .models import (Cart,Item)
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
