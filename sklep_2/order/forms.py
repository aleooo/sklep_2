import string

from django import forms

from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street', 'street_number', 'ZIP_code', 'town', 'country']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'last_name'}),
            'email': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'email'}),
            'phone_number': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'phone_number'}),
            'street': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'street'}),
            'street_number': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'street_number'}),
            'ZIP_code': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'ZIP_code'}),
            'town': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'town'}),
            'country': forms.TextInput(attrs={'class': 'address_form form-control', 'placeholder': 'country'}),
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
  
        