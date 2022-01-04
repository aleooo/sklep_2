from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.utils.translation import gettext_lazy as _
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Address, UserModel


class UserModelForm(UserCreationForm):

    class Meta:
        model = UserModel 
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username': forms.TextInput(attrs={'class': 'register_input form-control shadow-none', 'placeholder': _('username'), 'required': 'required'}),
                   'email': forms.TextInput(attrs={'class': 'register_input form-control shadow-none form-check-input', 'placeholder': _('email'), 'type': 'email', 'required': 'required'}),
                #    'number': PhoneNumberPrefixWidget(initial='PL', attrs={'class': 'phone_number_register  shadow-none  phonenumber font_size_1', 'minlength': '9', 'required': 'required'})
                }
        labels = {
            'username': _('Username'),
            'email': _('Email'),
            # 'number': _('Phone Number')
        }
                     
    error_messages = {
        'password_mismatch': _('The two password fields didn`t match'),
    }

class PersonalForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'number')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '^[A-ZŻŹŁ].*', 'placeholder': '-----'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '^[A-ZŻŹŁ].*', 'placeholder': '-----'}),
            'email': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'type': 'email', 'placeholder': '-----'}),
            'number': PhoneNumberPrefixWidget(initial='PL', attrs={'class': 'input font_numbers_light phonenumber form-control', 'placeholder': '-----', 'minlength': '9'}),
        }
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
            'number': _('Phone Number'),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'street_number', 'country', 'ZIP_code', 'town')
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '^[A-ZŻŹŁ].*', 'placeholder': '-----'}),
            'street_number': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'placeholder': '-----'}),
            'town': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '^[A-ZŻŹŁ].*', 'placeholder': '-----'}),
            'ZIP_code': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '[0-9-]*', 'placeholder': '-----'}),
            'country': forms.TextInput(attrs={'class': 'form-control font_numbers_light input', 'pattern': '^[A-ZŻŹŁ].*', 'placeholder': '-----'}),
        }
        labels = {
            'street': _('Street'),
            'street_number': _('Street Number'),
            'country': _('Country'),
            'ZIP_code': _('ZIP Code'),
            'town': _('Town')
        }
