from django import forms
from .models import Comment, ProductMen

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'stars', ]

class ProductmenForm(forms.ModelForm):
    class Meta:
        model=ProductMen
        fields = ['color' ,]


