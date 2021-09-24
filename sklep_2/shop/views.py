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
