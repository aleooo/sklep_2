from django.shortcuts import redirect, render

from order.models import OrderProduct

from .forms import OrderForm
from .utils import data
from cart.cart import Cart
from shop.models import Product


def order(request):
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            object_order = form.save()
            productOrder(request, object_order)
            return redirect('shop:main')
    else:
        if user.is_authenticated:
            form = OrderForm(initial=data(user))
        else:
            form = OrderForm()
    return render(request, 'content/order/order.html', {'form': form})


def productOrder(request, object_order):
    cart = Cart(request)
    for item in cart:
        product = Product.objects.get(id=int(item['id']))
        a = OrderProduct.objects.create(order=object_order, product=product, quantity=item['quantity'])
    cart.clear()
    
