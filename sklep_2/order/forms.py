import string

from django import forms
from django.utils.translation import gettext_lazy as _
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street', 'street_number', 'ZIP_code', 'town', 'country']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'last_name'}),
            'email': forms.TextInput(attrs={'class': 'address_form form-control margin_t_05', 'placeholder': 'email'}),
            'phone_number': PhoneNumberPrefixWidget(initial='PL', attrs={'class': 'address_form form-control phonenumber'}),
            'street': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'street'}),
            'street_number': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'street_number'}),
            'ZIP_code': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'ZIP_code'}),
            'town': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'town'}),
            'country': CountrySelectWidget(attrs={'class': 'address_form form-control', 'placeholder': 'country'}),
        }
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
            'phone_number': _('Phone Number'),
            'street': _('Street'),
            'street_number': _('Street Number'),
            'ZIP_code': _('ZIP code'),
            'town': _('Town'),
            'country': _('Country')
        }
    
    def clean(self):
        first_name = self.cleaned_data['first_name']
        field_upper = {'first_name': 'First Name', 'last_name': 'Last Name', 'street': 'Street', 'town': 'Town', 'country': 'Country'}

        for field in field_upper:
            if not self.cleaned_data[field][0].isupper():
                self.add_error(field, f'{field_upper[field]} should start with an uppercase letter')
       
        punctuation = string.punctuation
        for letter in first_name:
            if letter in punctuation:
                self.add_error('first_name', f"First Name should't contain punctuation")
                break
  
        