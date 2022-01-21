from shop.models import Product
from sklep_2 import settings
from decimal import Decimal


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        # In the session is created empty dictionary if there is no cart
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})
        # In the session is created empty dictionary if there is no coupon 
        self.session['coupon'] = self.session.get('coupon', {})
        
    # The method computes the total value of product
    def total_price_item(self, id):
        self.cart[id]['total_price'] = str(self.cart[id]['quantity'] * Decimal(self.cart[id]['price']))

    # It method adds a product to session 
    def add(self, product, quantity, modify_cart=False):
        id_product = str(product.id)

        # check if product exist in the cart session
        if id_product in self.cart:
            if modify_cart:
                # In the cart is set a total value
                self.cart[id_product]['quantity'] = quantity
            else:
                # In the detail product is added quantity to a total value
                self.cart[id_product]['quantity'] += quantity
            self.total_price_item(id_product)

        # if not In the session is created new object
        else:
            self.cart[id_product] = {'quantity': quantity, 'price': str(product.price), 'name': product.name, 'image': product.image.url, 'id': str(product.id)}
            self.total_price_item(id_product)

        # puts information to the session about an added product. 
        # This is for display window about success an added product to session
        if not modify_cart:
            self.session['add'] = True
        self.save()
        
    # when the session has been modified that don't neet to save
    # but if creates new key in dictionary. We must assign session.modified = True. 
    def save(self):
        self.session.modified = True

    def error(self, name):
        self.session['error'] = name
    
    # clear the session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.cart.clear()
        del self.session['coupon']
        self.save()

    # clear information about an added product
    def clear_add(self):
        if self.session.get('add', False):
            del self.session['add']
            return True
        return False
    
    # if discount of coupon is greater than the current the method coupon
    #  adds a discount and validity. 
    # the method isoformat formats datetime to string
    def coupon(self, coupon_obj):
        if coupon_obj:
            if coupon_obj.discount > float(self.session['coupon'].get('discount', 0)):
                self.session['coupon'] = {'discount':  str(coupon_obj.discount),
                                          'valid_from': coupon_obj.valid_from.isoformat(),
                                          'valid_to': coupon_obj.valid_to.isoformat()}
      

    # removes a specific product in the session
    def remove(self, id):
        del self.cart[str(id)]
   

    # iterates values in the dictionary of session
    def __iter__(self):
        for item in self.cart.values():
            yield item
    

    # computes the total value of the cart
    def total_value_cart(self):
        total_value = 0   

        for item in self.cart.values():
            total_value += Decimal(item['total_price'])
        total_value = float(total_value)    
        
        return total_value
    
    # computes the total value of the cart with discount
    def total_value_cart_after_discount(self):
        disc = self.session['coupon'].get('discount', 1)
        total_value = self.total_value_cart() * (1 - float(disc))
        total_value = float(total_value)

        return round(total_value, 2)

    # The method checks if there is a coupon
    def check_coupon(self):
        if self.session['coupon']:
            return True
        return False

    

    

        
        