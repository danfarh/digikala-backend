from django.urls import path, include
from category.api.urls import urlpatterns


app_name = 'categories'

urlpatterns = [
	path('api/', include(urlpatterns)),
]