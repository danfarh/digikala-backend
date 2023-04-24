from django.urls import path
from product.api import views
app_name='products'
urlpatterns = [
    #path('', views.ProductView.as_view() , name='products'),
    path('', views.ListCreateProductView.as_view() , name='products_listCreate'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductView.as_view() , name='products_listCreate'),
]