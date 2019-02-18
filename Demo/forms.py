from django import forms
from django.db.models.fields import CharField

class Login_Form(forms.Form):
    username=forms.CharField(max_length=35,required=True)
    password=forms.CharField(max_length=32,widget=forms.PasswordInput,required=True)
