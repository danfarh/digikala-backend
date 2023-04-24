from rest_framework import serializers
from ..models import Color,Image,Size,Product,ProductDiscount 
from category.api.serializers import CategorySerializer



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'                

class ProductDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDiscount
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    color = ColorSerializer(many=True)
    size = SizeSerializer(many=True)
    category = CategorySerializer()
    discount = ProductDiscountSerializer()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'slug','weight',
            'length','width',
            'status','price',
            'category',
            'discount',
            'image',
            'color',
            'size'
        ]
      
class CreateProductSerializer(serializers.ModelSerializer):
    length = serializers.DecimalField(max_digits=5, decimal_places=2,allow_null=True)
    width = serializers.DecimalField(max_digits=5, decimal_places=2,allow_null=True)
    class Meta:
        model = Product
        fields = ['title','description','slug','weight','length','width','status','price','category']

    def create(self,validated_data):
        p = Product(
            title = validated_data['title'],
	        slug = validated_data['slug'],
            category = validated_data['category'],
	        # color = self.context['color'],
	        # size = self.context['color'],
	        weight = validated_data['weight'],
	        length = validated_data['length'],
	        width = validated_data['width'],
	        status = validated_data['status'],
            price = validated_data['price']
        )  
        p.save()
        return p 
