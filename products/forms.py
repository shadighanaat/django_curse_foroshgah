from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'stars', ]

class CommentBlog(forms.ModelForm):
     class Meta:
        model = Comment
        fields = ['body', ]