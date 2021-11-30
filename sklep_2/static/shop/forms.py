from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.utils.translation import gettext_lazy as _

from .models import Address, UserModel


class UserModelForm(UserCreationForm):
    
    class Meta:
        model = UserModel 
        fields = ('username', 'email', 'password1', 'password2', 'number')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input', 'placeholder': _('username')}),
                   'email': forms.TextInput(attrs={'class': 'register_input', 'placeholder': _('email')}),
                   'password1': forms.TextInput(attrs={'class': 'register_input', 'placeholder': _('password')}),
                   'password2': forms.PasswordInput(attrs={'class': 'register_input', 'placeholder': _('password again')}),
                   'number': forms.PasswordInput(attrs={'class': 'register_input', 'placeholder': _('number')})}
    
    error_messages = {
        'password_mismatch': _('The two password fields didn`t match'),
    }

