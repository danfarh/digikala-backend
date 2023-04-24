from django.urls import path
from discount.api import views
app_name='discount'

urlpatterns = [
    path('', views.ListCreateDiscountView.as_view() , name='discounts'),
    path('<int:pk>/', views.RetrieveUpdateDestroyDiscountView.as_view() , name='discount'),
    path('check/', views.checkDiscountIsValid.as_view() , name='check_discount'),
]