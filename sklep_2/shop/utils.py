from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from order.models import OrderProduct
from shop.models import Product


def filter_prices_products(*args, **kwargs):
    data = args[0].GET
    filter = float(data.get('filter', 0))
    try:
        from_price = float(data.get('from', 0))
    except:
        from_price = 0
    try: 
        to_price = float(data.get('to', 1000000))
        if to_price < from_price:
            to_price = 1000000
    except:
        to_price = 1000000
    
    if filter:
        if filter == 20.0:
            products = args[1].filter(price__lt=filter)
        elif filter == 50.0:
            products =  args[1].filter(price__range=(20, 50))
        elif filter == 75.0:
            products =  args[1].filter(price__range=(50, 75))
        elif filter == 150.0:
            products =  args[1].filter(price__range=(75, 150))
        else:
            products =  args[1].filter(price__range=(150, 1000000))
    else:
        
        if from_price == to_price:
            products =  args[1].filter(price=from_price)
        else:
            products =  args[1].filter(price__range=(from_price, to_price))
    
    return products


def pagination(page, products):
    paginator = Paginator(products, 5)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects


# data without csrfmiddlewaretoken
def data_post(request):
    data = request.POST.copy()
    try:
        del data['csrfmiddlewaretoken']
    except KeyError:
        pass
    if 'number_0' in data:
        data['number'] = data.pop('number_0')[0] + data.pop('number_1')[0]
    return data    

# top 10 products on sale
def ranking():
    orders = OrderProduct.objects.all()
    rank = {}
    for order in orders:
        rank[order.product] = rank.setdefault(order.product, 0) + order.quantity
    return rank
