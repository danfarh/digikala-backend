from django.urls import path, include
from product.api.urls import urlpatterns


app_name = 'product'

urlpatterns = [
	path('api/', include(urlpatterns)),
]
