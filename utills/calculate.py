from django.shortcuts import get_object_or_404, render
from cart.cart import Cart
from cart.models import Cart as CartSchema
from cart.models import Item
from discount.models import Discount
from datetime import datetime
from django.core.cache import cache
from rest_framework.response import Response


def calculateDiscountCartPrice(request,code):
    cart_id = cache.get(f'{request.user}-cart')
    items = Item.objects.filter(cart=cart_id)
    if len(items) == 0:
        return {'message': 'cart is empty'}

    price = 0
    for item in items:
        price += item.price * item.quantity
    # calculate discount 
    if check_discount_code(code):
        discount = get_object_or_404(Discount,code=code)
        cart = CartSchema.objects.get(id=cart_id)    
        cart.discount = discount
        cart.save()
        cache.set(f'{request.user}-discount',discount.id,timeout=20*24*3600)           
        return {'message': 'done'}  
    return {'message': 'discount is expire'}   
          

def check_discount_code(code):
        discount = get_object_or_404(Discount,code=code)
        current_datetime = datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
        if discount:
            start_time = discount.start.strftime('%y-%m-%d %a %H:%M:%S') 
            end_time = discount.end.strftime('%y-%m-%d %a %H:%M:%S') 
            
            if start_time <= current_datetime <= end_time:
                return True
            else:
                return False
        return False

	  