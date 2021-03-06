from io import BytesIO
from math import e

from decimal import Decimal
from webbrowser import get
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic.base import View
import weasyprint

from .forms import OrderForm
from .models import Order
from .tasks import order_pdf
from .utils import data
from cart.cart import Cart
from order.models import OrderProduct, Parcel
from shop.models import Product, UserModel
from shop.recommender import Recommender
from sklep_2 import settings


# In admin site is generate pdf to each order
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('content/order/pdf.html', {'order': order})
    response = HttpResponse(headers={
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename="order_{order_id}.pdf"'})
    weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response)
    return response


def order(request):
    cart = Cart(request)
    user = request.user

    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)

        if form.is_valid():
            object_order = form.save(commit=False)

            # the condition checks if the user is registered
            if user.id:
                object_order.user = UserModel.objects.get(id=user.id)

            # the condition checks if the user use coupon
            if cart.session['coupon']:
                object_order.discount = Decimal(cart.session['coupon']['discount'])
            object_order.save()
            
            # In the database the function creates separate order products 
            # Each product is an order relation
            product_order(object_order, cart)
            # order_pdf generates pdf which is send on user's email
            order_pdf.delay(object_order.id)

            return redirect('shop:main')
    else:
        # check if the user is logged in. 
        if user.is_authenticated:
            # form automatically holds user's data
            form = OrderForm(initial=data(user))
        else:
            form = OrderForm()
    
    return render(request, 'content/order/order.html', {'form': form,
                                                        'main_bar': True})


def product_order(object_order, cart):
    # dictionary with data of products id and quantity
    # this data are needed for engine recommendation 
    recommendation_data = {}

    for item in cart:
        recommendation_data[item['id']] = item['quantity']
        product = Product.objects.get(id=int(item['id']))
        a = OrderProduct.objects.create(order=object_order, product=product, quantity=item['quantity'])

    r = Recommender()
    r.products_bought(recommendation_data)
    cart.clear()  


class ParcelView(View):
    def get(self, request, *args, **kwargs):
        data = list(Parcel.objects.values())
        return JsonResponse(data, safe=False)
    
      
