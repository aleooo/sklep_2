from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.test import client
from django.urls import reverse

from .forms import UserModelForm
from .models import Category, Product

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

def list(request, category=None):
    if category:
        cat = Category.objects.get(slug=category)
        products = Product.objects.filter(category=cat)
    elif request.method == 'POST':
        print(request.POST)
        products = Product.objects.filter(name__icontains=request.POST.get('search'))
    else:
        products = None
    
    return render(request, 'content/list.html', {'main_bar': True,
                                                 'products': products})
    



        
