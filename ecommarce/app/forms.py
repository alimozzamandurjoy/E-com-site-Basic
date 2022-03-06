from .models import *
from django import forms 
from django.contrib.auth.forms import UserCreationForm

class RegForms(UserCreationForm):
    class Meta:
        model= User
        fields= ['username','password1','password2']
