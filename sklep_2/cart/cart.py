from shop.models import Product
from decimal import Decimal

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.session['error'] = False
        self.session['add'] = False
        self.cart = self.session.setdefault('cart', {})
        
    def total_price_item(self, id):
        self.cart[id]['total_price'] = str(self.cart[id]['quantity'] * Decimal(self.cart[id]['price']))

    def add(self, product, quantity):
        id_product = str(product.id)
        if id_product in self.cart:
            self.cart[id_product]['quantity'] += quantity
            self.total_value_cart(id_product)
        else:
            self.cart[id_product] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url}
            self.total_value_cart(id_product)
        self.session['add'] = True
        
    
    def error(self, name):
        self.session['error'] = name
    
    def clear(self):
        del self.session['cart']


    def __iter__(self):
        for item in self.cart.values():
            yield item
    

    def total_value_cart(self):
        total_value = 0
        for item in self.cart.values():
            print(item)
            total_value += Decimal(item['total_price'])
        return total_value

    

    

        
        