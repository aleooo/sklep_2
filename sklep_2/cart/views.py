from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView

from .cart import Cart
from coupon.forms import CouponForm
from shop.models import Product
from shop.views import MainBar


class MainCart(TemplateView, MainBar):
    template_name = 'content/cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["coupon_form"] = CouponForm()
        return context

        
class RemoveItem(RedirectView):
    url = reverse_lazy('cart:main_cart')

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.remove(kwargs['id'])
        return super().get(request, *args, **kwargs)


def add_to_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    quantity = int(request.GET.get('quantity'))

    if request.GET.get('cart') == 'cart':
        cart.add(product=product, quantity=quantity, modify_cart=True)
        return redirect('cart:main_cart')
    else:
        cart.add(product=product, quantity=quantity)
        return redirect(product.get_absolute_url())    
