from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Address, UserModel


class UserModelForm(UserCreationForm):
    
    class Meta:
        model = UserModel 
        fields = ('username', 'email', 'password1', 'password2', 'number')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('username')}),
                   'email': forms.TextInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('email'), 'type': 'email'}),
                   'password1': forms.TextInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('password')}),
                   'password2': forms.PasswordInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('password again')}),
                     'number': PhoneNumberPrefixWidget(initial='PL', attrs={'class': 'register_input address_form form-control shadow-none  phonenumber'})}
                     
    error_messages = {
        'password_mismatch': _('The two password fields didn`t match'),
    }



