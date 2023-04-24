from django.urls import path, include
from .api.urls import urlpatterns


app_name = 'accounts'

urlpatterns = [
	# API accounts
	path('api/', include(urlpatterns)),
]
