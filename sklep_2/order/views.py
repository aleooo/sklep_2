from django.shortcuts import render

from .forms import OrderForm
from .utils import data


def orderView(request):
    user = request.user
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pass
    else:
        if user.is_authenticated:
            form = OrderForm(initial=data(user))
        else:
            form = OrderForm()
    return render(request, 'content/order.html', {'form': form})
    
