from django.contrib import admin
from .models import (Comment,Question,Answer)
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('title','confirm')
    search_fields = ('title','confirm')
    list_display = (
        'title',
        'text',
        'rate'
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('text','confirm')
    search_fields = ('text','confirm')
    list_display = (
        'user',
        'text',
        'confirm'
    )

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = ('text','confirm')
    search_fields = ('text','confirm')
    list_display = (
        'question',
        'text',
        'confirm'
    )        
