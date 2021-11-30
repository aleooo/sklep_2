from django import forms
from django.utils.translation import gettext_lazy as _

class CouponForm(forms.Form):
    code = forms.CharField(max_length=50)

    code.widget.attrs.update({'class': 'text_a_c border_1slg', 'id': 'coupon_input', 'placeholder': _('coupon')})
   
