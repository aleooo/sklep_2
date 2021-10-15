import string

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
    
    
    def clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        
        if not first_name[0].isupper():
            self.add_error('first_name', 'Should start with an uppercase letter')
        if not last_name[0].isupper():
            self.add_error('last_name', 'Should start with an uppercase letter')
        punctuation = string.punctuation
        for letter in first_name:
            if letter in punctuation:
                self.add_error('first_name', f"Should't contain punctuation")
                break
        for letter in last_name:
            if letter in punctuation:
                self.add_error('last_name', f"Should't contain punctuation")
                break
        