from django.urls import path
from cart.api import views
app_name='carts'
urlpatterns = [
    path('add/<int:product_id>/<int:quantity>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('get/', views.get_cart, name='get_cart'),
]