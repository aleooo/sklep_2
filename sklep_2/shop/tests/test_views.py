from django.test import TestCase
from django.contrib.auth.models import User
from django.urls.base import reverse

from shop.models import Products



class ViewTestCase(TestCase):
    def setUp(self):
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
    
    def test_main(self):
        response = self.client.get(reverse('shop:main'))
        self.assertContains(response, 'SHOP')