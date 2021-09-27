from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserModel


class UserModelForm(UserCreationForm):
    
    class Meta:
        model = UserModel 
        fields = ('username', 'email', 'password1', 'password2', 'number')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input', 'placeholder': 'username'}),
                   'email': forms.TextInput(attrs={'class': 'register_input', 'placeholder': 'email'}),
                   'password1': forms.TextInput(attrs={'class': 'register_input', 'placeholder': 'password'}),
                   'password2': forms.PasswordInput(attrs={'class': 'register_input', 'placeholder': 'password again'}),
                   'number': forms.PasswordInput(attrs={'class': 'register_input', 'placeholder': 'number'})}
    
    error_messages = {
        'password_mismatch': 'The two password fields didn`t match',
    }

