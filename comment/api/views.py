from django.conf import settings
from rest_framework.response import Response
from rest_framework import viewsets,generics
from ..models import Comment,Question,Answer
from .serializers import (CommentSerializer,QuestionSerializer,AnswerSerializer)
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

#pagination
class SetPagination(PageNumberPagination):
	page_size = settings.COMMENTS_PAGINATION
	page_size_query_param = 'page_size'
	max_page_size = settings.MAX_COMMENTS_PAGINATION

#######comment
class CommentView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #lookup_field = 'title'   

class CreateCommentView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = SetPagination

class CommentViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

#######question
class RetrieveQuestionView(generics.RetrieveAPIView): 
    queryset = Question.objects.filter(confirm=True)
    serializer_class = QuestionSerializer
    #lookup_field = 'title'   

class ListCreateQuestionView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Question.objects.filter(confirm=True)
    serializer_class = QuestionSerializer
    pagination_class = SetPagination
    filterset_fields = ['user','product','confirm']


#######answer
class RetrieveAnswerView(generics.RetrieveAPIView): 
    queryset = Answer.objects.filter(confirm=True)
    serializer_class = AnswerSerializer
    #lookup_field = 'title'   

class ListCreateAnswerView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Answer.objects.filter(confirm=True)
    serializer_class = AnswerSerializer
    pagination_class = SetPagination
    filterset_fields = ['user','question','confirm']