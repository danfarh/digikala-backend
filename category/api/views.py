from ..models import Category
from rest_framework import status,generics
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer 
      

class ListCreateProductView(generics.ListCreateAPIView): 
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer 
  