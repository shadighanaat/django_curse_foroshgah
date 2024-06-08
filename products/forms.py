from django import forms
from .models import Comment, ProductMen
from colorfield.fields import ColorField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'stars', ]

class ProductmenForm(forms.ModelForm):
    class Meta:
        model=ProductMen
        fields = ['color' ,]

   
# class ColorInput(forms.widgets.Input):
#     input_type = "color"

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = ProductMen
#         fields = '__all__'
#         widgets = {
#             'color': ColorInput(),
#         }
