from django import forms

from .models import Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street', 'street_number', 'ZIP_code', 'town', 'country']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'last_name'}),
            'email': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'email'}),
            'phone_number': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'phone_number'}),
            'street': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'street'}),
            'street_number': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'street_number'}),
            'ZIP_code': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'ZIP_code'}),
            'town': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'town'}),
            'country': forms.TextInput(attrs={'class': 'address_form', 'placeholder': 'country'}),
        }