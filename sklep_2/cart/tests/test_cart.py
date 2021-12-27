from django.http import HttpRequest
from django.test import TestCase

from cart.cart import Cart
from shop.models import Category, Product

class CartTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        self.product_1 = Product.objects.create(category=category,
                                name='Django 3',
                                slug='django_3',
                                description='practical web application development',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        self.product_2 = Product.objects.create(category=category,
                                name='Peak',
                                slug='peak',
                                description='Anyone who wants to get better at anything should read Peak',
                                price=49.99,
                                available=True,
                                quantity_available=4)
        request = self.client
        self.cart = Cart(request)
    
    def test_cart(self):
        self.assertEqual(self.cart.cart, {})
    
    def test_coupon(self):
        self.assertEqual(self.cart.session['coupon'], {})

    def test_cart_add(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)
        
        self.assertEqual(self.cart.cart[id]['quantity'], 2)
        self.assertEqual(self.cart.cart[id]['price'], '69.99')
        self.assertEqual(self.cart.cart[id]['name'], 'Django 3')
        self.assertEqual(self.cart.cart[id]['id'], id)
    
    def test_cart_add_total_price_item(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)

        self.assertEqual(self.cart.cart[id]['total_price'], '139.98')  


