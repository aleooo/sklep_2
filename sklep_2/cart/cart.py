from shop.models import Product
from decimal import Decimal

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.session['error'] = False
        self.session['add'] = False
        self.cart = self.session.setdefault('cart', {})
        
    
    def add(self, product, quantity):
        id_product = str(product.id)
        if id_product in self.cart:
            self.cart[id_product]['quantity'] += quantity
        else:
            self.cart[id_product] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url}
        self.session['add'] = True
        
    
    def error(self, name):
        self.session['error'] = name
    
    def clear(self):
        del self.session['cart']


    def __iter__(self):
        # id_products = self.cart.keys()
        # products = Product.objects.filter(id__in=id_products)
        # cart = self.cart.copy()
        # for product in products.values():
        #     self.cart[str(product['id'])]['product'] = product 
        
        for item in self.cart.values():
            item['total_price'] = str(item['quantity'] * Decimal(item['price']))
            yield item
        