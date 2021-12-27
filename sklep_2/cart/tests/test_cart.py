import datetime as d
import pytz
from decimal import Decimal

from django.http import HttpRequest
from django.test import TestCase

from cart.cart import Cart
from coupon.models import Coupon
from shop.models import Category, Product

class CartTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        self.product_1 = Product.objects.create(category=category,
                                name='Django 3',
                                slug='django_3',
                                description='''practical web application 
                                               development''',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        self.product_2 = Product.objects.create(category=category,
                                name='Peak',
                                slug='peak',
                                description='''Anyone who wants to get better
                                               at anything should read Peak''',
                                price=49.99,
                                available=True,
                                quantity_available=4)
        self.coupon_1 = Coupon.objects.create(code='1234abc', discount=0.30 ,
                                        valid_from=d.datetime(2021, 11, 24,
                                        tzinfo=pytz.UTC),
                                        valid_to=(d.datetime(2021, 11, 24,
                                        tzinfo=pytz.UTC) + d.timedelta(days=5)),
                                        active=True)

        self.coupon_2 = Coupon.objects.create(code='1124abc', discount=0.45 ,
                                        valid_from=d.datetime(2021, 11, 24,
                                        tzinfo=pytz.UTC),
                                        valid_to=(d.datetime(2021, 11, 24,
                                        tzinfo=pytz.UTC) + d.timedelta(days=5)),
                                        active=True)
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
    
    def test_cart_add_modify_cart(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)
        self.cart.add(self.product_1, 4, True)

        self.assertEqual(self.cart.cart[id]['quantity'], 4)
    
    def test_cart_add_if_a_product_is_in_the_cart_without_modified(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)
        self.cart.add(self.product_1, 4)

        self.assertEqual(self.cart.cart[id]['quantity'], 6)
    
    def test_cart_session_information_about_added_product(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)

        self.assertEqual(self.cart.session['add'], True)

    
    def test_cart_add_total_price_item(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)

        self.assertEqual(self.cart.cart[id]['total_price'], '139.98')  
    
    def test_cart_clear(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)
        self.cart.clear()

        self.assertEqual(self.cart.cart, {})
    
    def test_cart_clear_add(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)

        self.assertEqual(self.cart.clear_add(), True)
    
    def test_cart_coupon(self):
        self.cart.coupon(self.coupon_1)

        self.assertEqual(self.cart.session['coupon']['discount'], '0.3')
    
    def test_cart_coupons_discount_ascending_order(self):
        self.cart.coupon(self.coupon_1)
        self.cart.coupon(self.coupon_2)

        self.assertEqual(self.cart.session['coupon']['discount'], '0.45')
    
    def test_cart_coupons_discount_descending_order(self):
        self.cart.coupon(self.coupon_2)
        self.cart.coupon(self.coupon_1)

        self.assertEqual(self.cart.session['coupon']['discount'], '0.45')


    def test_cart_remove(self):
        id = str(self.product_1.id)
        self.cart.add(self.product_1, 2)
        self.cart.remove(id)

        self.assertEqual(self.cart.cart, {})
    
    def test_cart___iter__1(self):
        self.cart.add(self.product_1, 2)
        for product in self.cart:
            self.assertIn('name', product)
    
    def test_cart___iter__2(self):
        self.cart.add(self.product_2, 3)
        self.cart.add(self.product_1, 2)
        for product in self.cart:
            p = product
        self.assertEqual(2, p['quantity'])
    
    def test_total_value_cart(self):
        self.cart.add(self.product_2, 3)
        self.cart.add(self.product_1, 2)

        self.assertEqual(self.cart.total_value_cart(),
         (3 * self.product_2.price + 2 * self.product_1.price))
    
    def test_cart_total_value_cart_after_discount(self):
        self.cart.add(self.product_2, 3)
        self.cart.add(self.product_1, 2)
        self.cart.coupon(self.coupon_1)
        total_value_with_discount = ((1 - self.coupon_1.discount) *
         (3 * self.product_2.price + 2 * self.product_1.price))
        total_value_with_discount = round(total_value_with_discount, 2)

        self.assertEqual(self.cart.total_value_cart_after_discount(),
         total_value_with_discount)
    
    def test_cart_check_coupon(self):
        self.cart.coupon(self.coupon_1)

        self.assertEqual(self.cart.check_coupon(), True)
    
    def test_check_coupon_without_coupon(self):
        self.assertEqual(self.cart.check_coupon(), False)
