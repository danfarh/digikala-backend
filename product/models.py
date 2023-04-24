from django.db import models
from django.db.models.fields import BooleanField
from category.models import Category
from django.core.validators import MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from datetime import datetime,date



def product_image_path(instance, filename):
    now = datetime.now()
    return 'products/image/{0}/{1}/{2}/image_{3}/{4}'.format(
        now.strftime("%Y"),
        now.strftime("%m"),
        now.strftime("%d"),
		instance.id,
        filename)


class Brand(models.Model):
	en_name = models.CharField(max_length=200)
	fa_name = models.CharField(max_length=200)	
	
	def __str__(self):
		return self.en_name

class Size(models.Model):
	CHOICES_Size = (
		('s', 'small'),
		('m', 'medium'),
		('l', 'large')
	)
	size = models.CharField(choices=CHOICES_Size, max_length=1)
	def __str__(self):
		return self.size

class Color(models.Model):
    name = models.CharField(unique=True, max_length=30)
    code = models.CharField(unique=True, max_length=100)
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to=product_image_path,null=True)
    url = models.CharField(null=True, max_length=200)
    alt = models.CharField(null=True,blank=True, max_length=200)
    meta = models.CharField(null=True,blank=True, max_length=200)
    
    def __str__(self):
        return f'image-{self.id}'

class ProductDiscount(models.Model):
    percent = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
  
    def __str__(self):
        return f'product discount - {self.id}'

class Product(models.Model):
	CHOICES_STATUS = (
		('r', 'return'),
		('p', 'publish'),
		('d', 'draft')
		)

	title = models.CharField(max_length=50)
	description = models.TextField(null=True,blank=True)
	category = models.ForeignKey(
		Category,
		on_delete=models.SET_NULL,
		null=True,
		related_name='products'
		)
	discount = models.ForeignKey(
		ProductDiscount,
		on_delete=models.SET_NULL,
		null=True,
		blank=True
		)
	brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
	slug = models.SlugField(unique=True, allow_unicode=True, max_length=100)
	color = models.ManyToManyField(Color,blank=True,null=True)
	size = models.ManyToManyField(Size, blank=True,null=True)
	image = models.ManyToManyField(Image,blank=True,null=True)
	weight = models.DecimalField(max_digits=6, decimal_places=3)
	length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	width = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	price = models.DecimalField(max_digits=18, decimal_places=2)
	status = models.CharField(choices=CHOICES_STATUS, max_length=1)
	create = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return self.title

	def check_product_discount(self):
		current_datetime = datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
		if self.discount:
			start_time = self.discount.start.strftime('%y-%m-%d %a %H:%M:%S') 
			end_time = self.discount.end.strftime('%y-%m-%d %a %H:%M:%S') 
	       
			if start_time <= current_datetime <= end_time:
				return True
			else:
				return False
		return False

	@property
	def get_total_price(self):
		if self.check_product_discount:
			total = (self.discount.percent * self.price) / 100
			return int(self.price - total)
		return self.price					



	