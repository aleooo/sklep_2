from datetime import time
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from coupon.forms import CouponForm
from coupon.models import Coupon
from cart.cart import Cart

def coupon(request):
    cart = Cart(request)
    now = timezone.now()

    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            object = Coupon.objects.get(code=code, valid_from__lte=now, valid_to__gte=now)
        except ObjectDoesNotExist:
            object = None

        cart.coupon(object)

        return redirect('cart:main_cart')
        


  
    
    
