from django.urls import path
from comment.api import views
app_name='comments'
urlpatterns = [
    #retrieve & delete & update comments
    path('<int:pk>/', views.CommentView.as_view() , name='comments'),
    path('', views.CreateCommentView.as_view() , name='comments'),

    #retrieve & delete & update & create with viewsets
    path('list/', views.CommentViewSet.as_view({
        'get':'list',
        }) , name='lists'),
    path('create/<int:productId>/', views.CommentViewSet.as_view({
        'post':'create'
        }) , name='comments'),    
    path('<int:pk>/', views.CommentViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
        }) , name='comments'),


    #retrieve & create & list questions
    path('question/', views.ListCreateQuestionView.as_view() , name='questions'), 
    path('question/<int:pk>/', views.RetrieveQuestionView.as_view() , name='questions'),
   
    #retrieve & create & list answers
    path('answer/', views.ListCreateAnswerView.as_view() , name='answers'), 
    path('answer/<int:pk>/', views.RetrieveAnswerView.as_view() , name='answers'),
   
]