from rest_framework import fields, serializers
from ..models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class checkDiscountIsValidSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50,required=True)
            
