

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
            self.cart[id_product] = {'quantity': quantity, 'price': str(product.price), 'image': product.image.url}
        self.session['add'] = True
    
    def error(self, name):
        self.session['error'] = name

    
    
        
        
        

