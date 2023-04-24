from cart.models import Item
from product.models import Product
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User
from discount.models import Discount
#from cart.models import Cart

User = get_user_model()

class Order(models.Model):
    state_choices = (
        ("p" , "pending"),
        ("i" , "in-progress"),
        ("d" , "delivered"),
        ("r" , "returned"),
        ("c" , "canceled")
    )
    deliverMethod_choices =(
        ("e","express"),
        ("p","post")
    )
    paymentMethod_choices =(
        ("o" , "online"),
        ("c" , "cash")
    )
    amount = models.FloatField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(choices=state_choices,max_length=1) 
    deliverMethod = models.CharField(choices=deliverMethod_choices,max_length=1)
    paymentMethod = models.CharField(choices=paymentMethod_choices,max_length=1)
    items = models.ManyToManyField(Item,blank=True,null=True,related_name='items')
    discount= models.ForeignKey(
		Discount,
		on_delete=models.SET_NULL,
		null=True,
        blank=True
		)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.user.username}'


class Invoice(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    receiveTime = models.DateField()
    receiptCode = models.CharField(max_length=50) 
    trackingCode = models.CharField(max_length=50) 
    ShippingCost = models.CharField(max_length=50)  

  
