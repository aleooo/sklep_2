from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Address, UserModel


class UserModelForm(UserCreationForm):

    class Meta:
        model = UserModel 
        fields = ('username', 'email', 'number')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('username'), 'required': 'required'}),
                   'email': forms.TextInput(attrs={'class': 'register_input form-control shadow-none form-check-input', 'placeholder': _('email'), 'minlength': '3', 'type': 'email', 'required': 'required'}),
                   'number': PhoneNumberPrefixWidget(initial='PL', attrs={'class': 'phone_number_register form-control shadow-none  phonenumber font_size_1', 'minlength': '9', 'required': 'required'})}
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            'number': _('Phone Number')
        }
                     
    error_messages = {
        'password_mismatch': _('The two password fields didn`t match'),
    }



