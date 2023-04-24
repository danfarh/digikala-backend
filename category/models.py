from django.db import models

# Create your models here.
class Category(models.Model):
	parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
	title = models.CharField(max_length=200, verbose_name='title')
	slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')
	status = models.BooleanField(default=True, verbose_name='status')

	def __str__(self):
		return self.title
	
