from django.urls import path
from category.api import views
app_name='categories'
urlpatterns = [
    path('', views.ListCreateProductView.as_view() , name='list_categories'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductView.as_view() , name='categories'),   
]