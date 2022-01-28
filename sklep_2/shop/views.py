from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import ContextMixin

from shop.forms import UserModelForm, PersonalForm, AddressForm
from shop.models import Address, Category, Product, UserModel
from shop.recommender import Recommender
from shop.utils import filter_prices_products, data_post
 

class MainBar(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_bar'] = True
        return context


class Main(ListView, MainBar):
    model = Product
    template_name = 'content/shop/main.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
    
    def get_queryset(self):
        products = Product.objects.all()
        r = Recommender()
        queryset = r.popular_products(products)
        return queryset
    

class Register(CreateView):
    model = UserModel
    form_class = UserModelForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('shop:login')


class Detail(DetailView, MainBar):
    model = Product
    template_name = 'content/shop/detail.html'
    context_object_name = 'product'


class List(ListView, MainBar):
    model = Product
    template_name = 'content/shop/list.html'
    paginate_by = 5
    context_object_name = 'products'
    
    def get_queryset(self):
        if self.kwargs.get('category'):
            category = Category.objects.get(slug=self.kwargs.get('category'))
            queryset = Product.objects.filter(category=category)
        elif self.kwargs.get('search'):
            queryset = Product.objects.filter(name__icontains=self.kwargs.get('search'))
        else:
            queryset = Product.objects.all()
        if self.request.GET.get('filter'):
            queryset = filter_prices_products(self.request.GET, queryset)
        return queryset


@login_required
def account(request, type=None):
    user = UserModel.objects.get(id=request.user.id)
    orders = user.order.values('id', 'created')
       
    if request.method == 'POST':
        address = user.address
        # using own function which is the shop.utils.py throw away the csrftoken from request.POST
        data = data_post(request)

        # assigning data to an object
        if type == 'address':
            for k, v in data.items():  
                if k in address.__dict__:
                    setattr(address, k, v)
            address.save()
        elif type == 'personal_data':
            for k, v in data.items():
                if k in user.__dict__:
                    setattr(user, k, v)
            user.save()
        return redirect('shop:account')
           
    else:
        personal_form = PersonalForm(instance=user)
        address_form = AddressForm(instance=user.address)    
    

    return render(request, 'content/shop/account.html', {'address_form': address_form,
                                                    'main_bar': True,
                                                    'orders': orders,
                                                    'personal_form': personal_form,
                                                    'user': user}) 


def search(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        products = Product.objects.filter(name__icontains=text)[:8]
        data = []
        if len(products) > 0 and len(text) > 0:     
            for product in products:
                data.append(product.data())
        return JsonResponse({'data': data})
