from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView

from shop.forms import UserModelForm, PersonalForm, AddressForm
from shop.models import Address, Category, Product, UserModel
from shop.recommender import Recommender
from shop.utils import filter_prices_products, data_post
 

def main(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    r = Recommender()
    
    products = r.popular_products(products)

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
                data.append(product.data())
        return JsonResponse({'data': data})

# Function url has few parameters that don't use
def detail(request, slug, *args, **kwargs):
    product = Product.objects.get(slug=slug)
    return render(request, 'content/detail.html', {'product': product,
                                                   'main_bar': True,
                                                   })


class List(ListView):
    model = Product
    template_name = 'content/list.html'
    paginate_by = 5
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_bar'] = True
        return context
    
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
    

    return render(request, 'content/account.html', {'address_form': address_form,
                                                    'main_bar': True,
                                                    'orders': orders,
                                                    'personal_form': personal_form,
                                                    'user': user}) 



