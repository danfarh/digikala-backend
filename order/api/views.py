from ..models import Order
from django.shortcuts import get_object_or_404, render
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializers import OrderSerializer,CreateOrderSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.cache import cache
from cart.models import Item
from cart.cart import Cart
from discount.models import Discount

def calculateCartPrice(request,order,items):
    discount_id = cache.get(f'{request.user}-discount')
    price = 0
    for item in items:
        price += item.price * item.quantity
        order.items.add(item)

    if discount_id:
        discount = get_object_or_404(Discount,id=discount_id)
        order.discount = discount  
        price = price * (100 - discount.percent) / 100
        order.amount = price
        order.save()
        cache.delete(f'{request.user}-discount')
    else:
        order.amount = price
        order.save()       
    
    cart = Cart(request)
    cart.clear()


class CreateOrderView(generics.GenericAPIView): 
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateOrderSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.POST)
        
        if serializer.is_valid():
            cart_id = cache.get(f'{request.user}-cart')
            items = Item.objects.filter(cart=cart_id)
        
            if len(items) != 0:
                order = Order.objects.create(
                    state='p',
                    deliverMethod=serializer.data.get('deliverMethod'),
                    paymentMethod=serializer.data.get('paymentMethod'),
                    user=request.user
                )
                #calculate cart price
                calculateCartPrice(request,order,items)   
                return  Response({'message':'create order successfully'},status.HTTP_200_OK)  
            else:
                return Response({'message': 'cart is empty'})         
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)            
   

class ListOrderView(generics.ListAPIView): 
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer


class RetrieveUpdateDestroyOrderView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]



         