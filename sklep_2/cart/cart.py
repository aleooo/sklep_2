from shop.models import Product
from sklep_2 import settings
from decimal import Decimal


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})
        self.session['coupon'] = self.session.get('coupon', {})
        
    def total_price_item(self, id):
        self.cart[id]['total_price'] = str(self.cart[id]['quantity'] * Decimal(self.cart[id]['price']))

    def add(self, product, quantity, modify_cart=False):
        id_product = str(product.id)
        if id_product in self.cart:
            if modify_cart:
                self.cart[id_product]['quantity'] = quantity
            else:
                self.cart[id_product]['quantity'] += quantity
            self.total_price_item(id_product)
        else:
            self.cart[id_product] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url, 'id': str(product.id)}
            self.total_price_item(id_product)
        if not modify_cart:
            self.session['add'] = True
        self.save()
        
    
    def save(self):
        self.session.modified = True

    def error(self, name):
        self.session['error'] = name
    
    def clear(self):
        del self.session['cart']
        self.save()

    def clear_add(self):
        if self.session.get('add', False):
            del self.session['add']
            return True
        return False
    
    def coupon(self, coupon_obj):
        if coupon_obj:
            if coupon_obj.discount > self.session['coupon'].get('discount', 0):
                self.session['coupon'] = {'discount':  str(coupon_obj.discount), 'valid_from': coupon_obj.valid_from.isoformat(), 'valid_to': coupon_obj.valid_to.isoformat()}
      

    def remove(self, id):
        del self.cart[str(id)]
        self.save()

    def __iter__(self):
        for item in self.cart.values():
            yield item
    

    def total_value_cart(self):
        total_value = 0
        coupon = self.session['coupon'].get('discount', None)

        for item in self.cart.values():
            total_value += Decimal(item['total_price'])
        if coupon:
            total_value *= (1 - Decimal(coupon))

        return round(total_value, 2)

    

    

        
        