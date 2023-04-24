import datetime
from django.db.models import Sum
from django.db.models import F
from . import models

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            cart = models.Cart.objects.filter(id=cart_id, checked_out=False).first()
            if cart is None:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def get_cart_id(self):
        for item in self.cart.item_set.all():
            return item.cart.id
            
    def new(self, request):
        cart = models.Cart.objects.create(creation_date=datetime.datetime.now())
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, price, quantity=1):
        item = models.Item.objects.filter(cart=self.cart, product=product).first()
        if item:
            item.price = price
            item.quantity += int(quantity)
            item.save()
        else:
            models.Item.objects.create(cart=self.cart, product=product, price=price, quantity=quantity)

    def remove(self, product):
        item = models.Item.objects.filter(cart=self.cart, product=product).first()
        if item:
            item.delete()
        else:
            raise ItemDoesNotExist

    def update(self, product, quantity, price=None):
        item = models.Item.objects.filter(cart=self.cart, product=product).first()
        if item:
            if quantity == 0:
                item.delete()
            else:
                item.price = price
                item.quantity = int(quantity)
                item.save()
        else:
            raise ItemDoesNotExist

    def count(self):
        return self.cart.item_set.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def summary(self):
        return self.cart.item_set.all().aggregate(total=Sum(F('quantity')*F('price'))).get('total', 0)

    def clear(self):
        self.cart.delete()

    def is_empty(self):
        return self.count() == 0

    def cart_serializable(self):
        representation = {}
        for item in self.cart.item_set.all():
            item_id = str(item.object_id)
            item_dict = {
                'total_price': item.total_price,
                'quantity': item.quantity
            }
            representation[item_id] = item_dict
        return representation