from rest_framework import serializers
from ..models import Order
from accounts.api.serializrs import UserRegisterSerializer
from cart.api.serializers import CartItemsSerializer
from discount.api.serializers import DiscountSerializer

class OrderSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    items = CartItemsSerializer(many=True)
    discount = DiscountSerializer()
    class Meta:
        model = Order
        exclude = ['update']

class CreateOrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = ['deliverMethod','paymentMethod']
            
