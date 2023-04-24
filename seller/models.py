from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Seller(models.Model):
    COMPANY_CHOICES = (
        ("pu" , "public"),
        ("pr" , "private"),
        ("l" ,"limited" ),
        ("c" , "coop")
    )
    GENDER_CHOICES = (
        ("m" , "Male"),
        ("f" , "Female")
    )
    first_name = models.EmailField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100,validators=[MinLengthValidator(8)])
    phoneNumber = models.CharField(max_length=200)
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    gender = models.CharField(max_length=1 , choices=GENDER_CHOICES)
    companyName = models.CharField(max_length=200)
    companyType = models.CharField(max_length=2, choices=COMPANY_CHOICES)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=200)
