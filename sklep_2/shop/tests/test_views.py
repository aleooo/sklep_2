from django.test import TestCase
from django.contrib.auth.models import User
from django.urls.base import reverse

from shop.models import Product, UserModel, Address
from shop.views import register



class ViewTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Django 3',
                                slug='django_3',
                                description='practical web application development',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        Product.objects.create(name='Peak',
                                slug='peak',
                                description='Anyone who wants to get better at anything should read Peak',
                                price=49.99,
                                available=True,
                                quantity_available=4)
        address = Address.objects.create(street='Krotka', street_number='3', ZIP_code='08-116', town='Seroczyn', country='Poland')
        UserModel.objects.create(username='aleo', first_name='alek', last_name='wiedenski', email='dwdawdw@gmail.com', password='aleoaleo', address=address, number='333333333')
    
    def test_main(self):
        response = self.client.get(reverse('shop:main'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_page(self):
        response = self.client.get(reverse('shop:login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        response = self.client.get(reverse('shop:register'))
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        query = {
         'username': 'aleoo', 'email': '',
          'password1': 'alekoaleko', 'password2': 'alekoaleko',
           'number': ''}
        response = self.client.post(reverse('shop:register'), data=query)
        self.assertEqual(response.status_code, 302)
    
    # def test_login(self):
    #     response = self.client.post(reverse('shop:login'), data={'username': 'aleo', 'password': 'aleoaleo'})
    #     self.assertEqual(response.status_code, 302)
        
