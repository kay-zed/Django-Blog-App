from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BlogTopic, BlogEntry, Comment

class BlogTopicForm(forms.ModelForm):
    class Meta:
        model = BlogTopic
        fields = ['title']
        labels = {'title' : ''}

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        fields = ['body']
        labels = {'body': ''}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['added_by', 'text']
