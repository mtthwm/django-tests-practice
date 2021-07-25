from django.forms import ModelForm, Form
from django import forms
from homepage.models import User, BlogPost

class UserForm (ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    