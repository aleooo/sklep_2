from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from order.models import OrderProduct
from shop.models import Product


def filter_prices_products(*args, **kwargs):
    data = args[0].GET
    filter = data.get('filter')
    try:
        from_price = int(data.get('from', 0))
    except:
        from_price = 0
    try: 
        to_price = int(data.get('to', 1000000))
    except:
        to_price = 1000000

    if filter:
        filter = int(filter)
        if filter == 20:
            return args[1].filter(price__lt=filter)
        elif filter == 50:
            return args[1].filter(price__range=(20, 50))
        elif filter == 75:
            return args[1].filter(price__range=(50, 75))
        elif filter == 150:
            return args[1].filter(price__range=(75, 150))
        else:
            return args[1].filter(price__range=(150, 1000000))
    else:
        return args[1].filter(price__range=(from_price, to_price))


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
