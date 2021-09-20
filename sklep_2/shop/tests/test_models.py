from django.test import TestCase
from django.contrib.auth.models import User

from shop.models import Products, Category


class ModelsTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        Products.objects.create(name='Django 3',
                                slug='django_3',
                                description='practical web application development',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        Products.objects.create(name='Peak',
                                slug='peak',
                                description='Anyone who wants to get better at anything should read Peak',
                                price=49.99,
                                available=True,
                                quantity_available=4)
                                
    def test_model_Category(self):
        category = Category.objects.first()
        self.assertEqual(category.name, 'Books')

    def test_model_Product(self):
        products = Products.objects.all()
        self.assertEqual(len(products), 2)
    
