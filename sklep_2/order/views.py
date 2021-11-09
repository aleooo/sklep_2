from io import BytesIO
from math import e
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

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
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
    return response


def order(request):
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            object_order = form.save()
            product_order(request, object_order)

            names_products = 'You ordered: ' + ',  '.join([product.product.name for product in object_order.products.all()])
            email = EmailMessage(subject=names_products, from_email=settings.EMAIL_HOST_USER, to=[object_order.email])
            html = render_to_string('content/order/pdf.html', {'order': object_order})
            out = BytesIO()
            #Must add STATIC_ROOT and make collectstatic in development
            weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(out)
            email.attach( f'order_{object_order.id }.pdf', out.getvalue(), 'application/pdf')
            email.send()

            return redirect('shop:main')
    else:
        if user.is_authenticated:
            form = OrderForm(initial=data(user))
        else:
            form = OrderForm()
    return render(request, 'content/order/order.html', {'form': form,
                                                        'main_bar': True})


def product_order(request, object_order):
    cart = Cart(request)
    for item in cart:
        product = Product.objects.get(id=int(item['id']))
        a = OrderProduct.objects.create(order=object_order, product=product, quantity=item['quantity'])
    cart.clear()
    
