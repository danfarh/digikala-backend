from ..models import Discount
from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import DiscountSerializer,checkDiscountIsValidSerializer
from discount.api import serializers
from rest_framework.response import Response
from utills.calculate import calculateDiscountCartPrice

class ListCreateDiscountView(generics.ListCreateAPIView): 
    queryset = Discount.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DiscountSerializer


class RetrieveUpdateDestroyDiscountView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Discount.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = DiscountSerializer

class checkDiscountIsValid(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = checkDiscountIsValidSerializer
    def get(self,request):
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid():
            code = serializer.data.get('code')
            result = calculateDiscountCartPrice(request,code)
            return Response({'result':result})
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)   
 

