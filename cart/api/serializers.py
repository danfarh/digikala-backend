from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..models import Cart,Item
from product.api.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()
    class Meta:
        model = Item
        fields = ['quantity','price','cart','total_price','product']