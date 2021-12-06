from django.core import serializers
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.test import client
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic.list import ListView

from cart.cart import Cart
from .forms import UserModelForm
from .models import Category, Product, UserModel
from .utils import filter_prices_products, pagination, data_post

import json 


def main(request):
  
    categories = Category.objects.all()
    products = Product.objects.all()
    if len(products) > 8 :
        products = products[:8]

    return render(request, 'content/main.html', {'main_bar': True,
                                                 'categories': categories,
                                                 'products': products})


def register(request):
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('shop:login')
    else:
        user_form = UserModelForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def search(request):
    if request.is_ajax():
        text = request.POST.get('text')
        products = Product.objects.filter(name__icontains=text)[:8]
        data = []
        if len(products) > 0 and len(text) > 0:     
            for product in products:
                item =  {
                    'id': product.id,
                    'name': product.name,
                    'image': str(product.image.url),
                    'price': product.price,
                    'description': product.description,
                    'url': product.get_absolute_url()
                }
                data.append(item)
        return JsonResponse({'data': data})


def detail(request, slug, **kwargs):
    product = Product.objects.get(slug=slug)
    return render(request, 'content/detail.html', {'product': product,
                                                   'main_bar': True,
                                                   })

def list(request, category=None, text=None):
    if category:
        cat = Category.objects.get(slug=category)
        products = Product.objects.filter(category=cat)
    elif request.method == 'GET':
        return redirect(reverse('shop:list_search', args=[request.GET.get('search')]))
    else:
        products = None
    products = filter_prices_products(request, products)
    page = request.GET.get('page')
    objects_pagination = pagination(products, page)
        
    return render(request, 'content/list.html', {'main_bar': True,
                                                 'objects': objects_pagination})


def list_search(request, text):
    products = Product.objects.filter(name__icontains=text)
    products = filter_prices_products(request, products)
    page = request.GET.get('page')
    objects_pagination = pagination(products, page)
    
    return render(request, 'content/list.html', {'main_bar': True,
                                                 'objects': objects_pagination})


def account(request):
    user = UserModel.objects.get(id=request.user.id)
    orders = user.order.values('id', 'created')
    address = {'town':{'value':'no town','field':'Town'},
                'ZIP_code':{'value':'no ZIP code','field':'ZIP code'},
                'country':{'value':'no country','field':'Country'},
                'street_number':{'value':'no street number','field':'Street number'},
                'street':{'value':'no street','field':'Street'}}
    for field, value in user.address.__dict__.items():
        if field not in ['_state', 'id']:
            if value: 
                address[field]['value'] = value

    address_json = json.dumps(address)

    return render(request, 'content/account.html', {'main_bar': True,
                                                    'orders': orders,
                                                    'address': address,
                                                    'address_json': address_json}) 

def account_data(request, type):
    user = request.user
    address = request.user.address
    if request.method == 'POST':
        data = data_post(request)
    
        if type == 'address':
            for k, v in data.items():
                setattr(address, k, v)
                address.save()
        else:
            for k, v in data.items():
                setattr(user, k, v)
                address.save()
    return redirect('shop:account')




    



        
