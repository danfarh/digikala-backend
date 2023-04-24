from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User
from product.models import Product
User = get_user_model()
# Create your models here.
class Comment(models.Model):
    RATE_CHOICES = (
        ('5', 'excellent'),
        ('4', 'very good'),
        ('3', 'good'),
        ('2', 'bad'),
        ('1', 'very bad')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='products')
    text = models.CharField(max_length=500)
    title =  models.CharField(max_length=150)
    rate = models.CharField(choices=RATE_CHOICES, max_length=1)
    confirm = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    confirm = models.BooleanField(default=False)

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField()
    confirm = models.BooleanField(default=False)    