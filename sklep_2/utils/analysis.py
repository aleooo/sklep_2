from order.models import OrderProduct
from shop.models import Product


# top 10 products on sale
def ranking():
    orders = OrderProduct.objects.all()
    rank = {}
    for order in orders:
        rank[order.product] = rank.setdefault(order.product, 0) + order.quantity
    return rank
    