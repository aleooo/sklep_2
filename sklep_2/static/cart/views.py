from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import Product


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
        

def remove_item(request, id):
    cart = Cart(request)
    cart.remove(id)
    return redirect('cart:main_cart')


def main_cart(request):
    return render(request, 'content/cart/cart.html', {'main_bar': True})

    

