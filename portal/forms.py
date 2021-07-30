from django import forms
from django.contrib import admin
from .models import *

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = []
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Digite o nome do autor','minlength': 3, 'maxlength': 255}),
            'surname': forms.TextInput(attrs={'placeholder': 'Digite o sobrenome do autor','minlength': 2, 'maxlength': 255}),
            'citation': forms.TextInput(attrs={'placeholder': 'Digite a citação do autor'}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título da obra', 'maxlength': 255}),
        }