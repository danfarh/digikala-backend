from django.db.models import manager
from cart.models import Item
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from product.models import Product
from utills.redis import redis_set,redis_get
from django.core.cache import cache
from .serializers import CartSerializer,CartItemsSerializer

login_required()
def add_to_cart(request, product_id, quantity):
    product = get_object_or_404(Product,id=product_id)
    cart = Cart(request)
    #cart.add(product, product.price, quantity)
    cart.add(product, product.get_total_price, quantity)
    cache.set(f'{request.user}-cart',str(cart.get_cart_id()),timeout=20*24*3600) #20 days
    #redis_set(f'{request.user}-cart',str(cart.get_cart_id()))
    return HttpResponse('added to cart successfully')

login_required()
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return HttpResponse('removed from cart successfully')
    
login_required()
def get_cart(request):
    #cart = redis_get(f'{request.user}-cart')
    #cart = Cart(request)
    cart_id = cache.get(f'{request.user}-cart')
    items = Item.objects.filter(cart=cart_id)
    if items is not None:
        serializer = CartItemsSerializer(items,many=True)
        return JsonResponse({'data': serializer.data}) 
    return JsonResponse({'failed': 'cart expired!'})    
    
  
    