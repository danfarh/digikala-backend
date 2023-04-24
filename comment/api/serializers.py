from product.models import Product
from rest_framework import serializers
from ..models import Comment,Question,Answer
from accounts.api.serializrs import UserRegisterSerializer
from product.api.serializers import ProductSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    product = ProductSerializer()
    class Meta:
        model = Comment
        fields = ['text','title','rate','confirm','user','product']

class QuestionSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    product = ProductSerializer()
    class Meta:
        model = Question
        fields = ['text','title','user','product']        

class AnswerSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()
    question = QuestionSerializer()
    class Meta:
        model = Answer
        fields = ['text','user','question']    