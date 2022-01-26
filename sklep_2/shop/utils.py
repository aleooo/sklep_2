from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from order.models import OrderProduct
from shop.models import Product


def price_range(*args, **kwargs):
    p = {'20': [0, 20],
         '50': [20, 50],
         '75': [50, 75],
         '150': [75, 150],
         '99999': [150, 99999]}
    filter = str(args[0])

    if filter in p:
        value = p[filter]
        return value[0], value[1]
    else:
        return 0, 99999


def filter_prices_products(*args, **kwargs):
    data = args[0]
    filter = data.get('filter', 'manual')

    if filter == 'manual':
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

        if from_price == to_price:
            products =  args[1].filter(price=from_price)
        else:
            products =  args[1].filter(price__range=(from_price, to_price))
    else:
        products = args[1].filter(price__range=(price_range(filter)))
    return products


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


