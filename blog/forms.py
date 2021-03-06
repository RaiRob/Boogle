from django import forms
from django.db import models
from django.forms import fields, widgets
from.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
		'author': forms.Select(attrs={'class': 'form-control'}),
		'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Body"}),
        }