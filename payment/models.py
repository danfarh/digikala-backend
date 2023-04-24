from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from order.models import Order
from accounts.models import User
# Create your models here.

User = get_user_model()

class Payment(models.Model):
    amount = models.FloatField(verbose_name='مقدار')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)
