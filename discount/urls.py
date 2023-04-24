from django.urls import path, include
from discount.api.urls import urlpatterns


app_name = 'discount'

urlpatterns = [
	path('api/', include(urlpatterns)),
]