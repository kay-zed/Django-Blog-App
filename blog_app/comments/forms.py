from .models import Comment
from django import forms

class CommentForm(form.ModelForm):
    def Meta:
        model = Comment
        fields = ['name', 'email', 'text']
