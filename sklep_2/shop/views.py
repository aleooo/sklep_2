import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http.response import JsonResponse
from django.contrib import messages 
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import resolve
from django.utils.translation import gettext_lazy as _

from cart.cart import Cart
from .forms import UserModelForm, PersonalForm, AddressForm
from .models import Address, Category, Product, UserModel
from .utils import filter_prices_products, pagination, data_post
 

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
    if request.method == 'POST':
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


def detail(request, slug, *args, **kwargs):
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
    
    # objects pagination
    page = request.GET.get('page')
    objects_pagination = pagination(page, products)
        
    return render(request, 'content/list.html', {'main_bar': True,
                                                 'objects': objects_pagination})


def list_search(request, text):
    products = Product.objects.filter(name__icontains=text)
    # filter out products with given price range in the request
    products = filter_prices_products(request, products)
    # objects pagination
    page = request.GET.get('page')
    objects_pagination = pagination(page, products)               
    
    return render(request, 'content/list.html', {'main_bar': True,
                                                 'objects': objects_pagination})


@login_required
def account(request, type=None):
    user = UserModel.objects.get(id=request.user.id)
    orders = user.order.values('id', 'created')
       
    if request.method == 'POST':
        if type == 'personal_data':
            data = request.POST
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.number = data['number_0'] + data['number_1']
            user.save()
            # personal_form = PersonalForm(request.POST)
            # if personal_form.is_valid():
            #     personal_form.save()
       
            return redirect('shop:account')
           
        elif type == 'address':
            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = address_form.save()
                user.address = address
                user.save()
                return redirect('shop:account')
    else:
        personal_form = PersonalForm(instance=user)
        address_form = AddressForm(instance=user.address)    
    

    return render(request, 'content/account.html', {'address_form': address_form,
                                                    'main_bar': True,
                                                    'orders': orders,
                                                    'personal_form': personal_form,
                                                    'user': user}) 


