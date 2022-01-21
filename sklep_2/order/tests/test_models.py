from decimal import Decimal

from django.test import TestCase

from order.models import Order, OrderProduct
from shop.models import Product, Address, Category


class OrderModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        self.product = Product.objects.create(category=category,
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
        
        self.order = Order.objects.create(first_name='Alek', last_name='Wiedenski', street='Krotka', street_number='3', ZIP_code='08-116', town='Seroczyn', country='Poland')

        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=3)
        self.order_product_2 = OrderProduct.objects.create(order=self.order, product=self.product_2, quantity=2)
    
    def test_Order(self):
        self.assertEqual(self.order.first_name, 'Alek')
    
    def test_Order_Product(self):
        self.assertEqual(self.order_product.quantity, 3)
    
    def test_Order_Product_total_price(self):
        self.assertEqual(self.order_product.total_price(), self.product.price * self.order_product.quantity)
    
    def test_Order_total_price(self):
        self.assertEqual(self.order.total_price(), Decimal(str((self.product.price * self.order_product.quantity) + (self.product_2.price * self.order_product_2.quantity))))

