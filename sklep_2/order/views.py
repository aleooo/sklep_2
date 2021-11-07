from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string

import weasyprint

from .forms import OrderForm
from .models import Order
from .utils import data
from cart.cart import Cart
from order.models import OrderProduct
from shop.models import Product
from sklep_2 import settings


def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('content/order/pdf.html', {'order': order})

    response = HttpResponse(headers={
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename="order_{order_id}.pdf"'})

    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        'templates/static/assets/css/base.css')])
    return response


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
    return render(request, 'content/order/order.html', {'form': form,
                                                        'main_bar': True})


def productOrder(request, object_order):
    cart = Cart(request)
    for item in cart:
        product = Product.objects.get(id=int(item['id']))
        a = OrderProduct.objects.create(order=object_order, product=product, quantity=item['quantity'])
    cart.clear()
    
