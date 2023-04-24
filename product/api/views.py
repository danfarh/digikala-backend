from django.conf import settings
from ..models import Product
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer,CreateProductSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny


# Create your views here.

#pagination
class SetPagination(PageNumberPagination):
	page_size = settings.PRODUCTS_PAGINATION
	page_size_query_param = 'page_size'
	max_page_size = settings.MAX_PRODUCTS_PAGINATION

class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        p = CreateProductSerializer(products,many=True)
        return Response(p.data)

    def post(self , request):
        p = CreateProductSerializer(
            data=request.POST
        )
        if p.is_valid():
            p.save()
            return Response(
                {
                    'message' : 'product created successfully',
                    'product':p.data
                },status=status.HTTP_200_OK)
        else:
            return Response({'message' : p.errors},status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return CreateProductSerializer 
        else:
            return ProductSerializer    

class ListCreateProductView(generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = SetPagination
    filterset_fields = ['category','status']
    search_fields = ['title','description','status','category__title']
    ordering_fields = ['create','status']  
    ordering = ['-create']
   
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]         
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        else:
            return CreateProductSerializer
