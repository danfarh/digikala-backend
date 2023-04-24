from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Discount(models.Model):
    CONDITION_CHOICES = (
        ('t','TIMELY'),
        ('f','FIRST_ORDER'),
        ('p','PERCENTAGE')
    )
    condition = models.CharField(max_length=1,choices=CONDITION_CHOICES)
    reason = models.CharField(max_length=500,null=True,blank=True)
    code = models.CharField(max_length=30,unique=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    expire = models.DateField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    active = models.BooleanField(default=False)
    percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.code  


  
  
  

     