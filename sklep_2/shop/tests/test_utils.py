from django.http import HttpRequest
from django.test import TestCase

from shop.models import Address, Category, Product
from shop.utils import filter_prices_products, data_post


class ShopUtilsTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        Product.objects.create(category=category,
                                name='Django 3',
                                slug='django_3',
                                description='practical web application development',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        Product.objects.create(category=category,
                                name='Peak',
                                slug='peak',
                                description='Anyone who wants to get better at anything should read Peak',
                                price=49.99,
                                available=True,
                                quantity_available=4)
        address = Address.objects.create(street='Krotka', street_number='3', ZIP_code='08-116', town='Seroczyn', country='Poland')
        self.products = Product.objects.all()
    
    def test_filter_prices_products_from_price_and_to_price(self):
        
        data = {'filter': 'manual', 'from': 60.00, 'to': 70.00}
        objects = filter_prices_products(data, self.products)
        self.assertQuerysetEqual(objects[0].name, 'Django 3')
    
    def test_filter_prices_products_filter_20(self):
        
        data = {'filter': 20}
        objects = filter_prices_products({'filter': 20}, self.products)
        self.assertEqual(list(objects), [])
    
    def test_filter_prices_products_filter_50(self):
        
        data = {'filter': 50}
        objects = filter_prices_products(data, self.products)
        self.assertEqual(objects[0].name, 'Peak')
    
    def test_filter_prices_products_filter_75(self):
        
        data = {'filter': 75}
        objects = filter_prices_products(data, self.products)
        self.assertEqual(objects[0].name, 'Django 3')
    
    def test_filter_prices_products_filter_150(self):
        
        data = {'filter': 150}
        objects = filter_prices_products(data, self.products)
        self.assertEqual(list(objects), [])

    def test_data_post_with_csrftoken(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {'csrfmiddlewaretoken': '12faw%$2a1', 'key': 'value'}

        self.assertEqual(data_post(request), {'key': 'value'})
    
    def test_data_post_without_csrftoken(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = {'key': 'value'}

        self.assertEqual(data_post(request), {'key': 'value'})

