# _*_ coding: utf-8 _*_
from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'description')
        labels = {
            'image' : 'Image',
            'description' : 'Description'
        }