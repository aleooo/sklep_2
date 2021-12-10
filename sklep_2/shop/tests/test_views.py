from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls.base import reverse

from shop.models import Address, Category, Product, UserModel
from shop.views import register



class ViewTestCase(TestCase):
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
        UserModel.objects.create(username='aleo', first_name='alek', last_name='wiedenski', email='dwdawdw@gmail.com', password='aleoaleo', address=address, number='333333333')
        c = Client()
        self.user = c.login(username='aleo', password='aleoaleo')
    
    def test_Main(self):
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
    
    def test_detail(self):
        product = Product.objects.first()
        response = self.client.get(product.get_absolute_url())  
        self.assertContains(response, 'Peak')
    
    def test_list_search(self):
        response = self.client.get(reverse('shop:list_search', args=['p']))
        self.assertContains(response, 'Peak')
    
    def test_list_redirect_search(self):
        response = self.client.get(reverse('shop:list'), data={'search': 'p'})
        self.assertEqual(response.status_code, 302)
        
    def test_list_Category(self):
        response = self.client.get(reverse('shop:list_category', args=['books']))
        self.assertContains(response, 'Django 3')
    
    def test_list_filter_prices_products(self):
        response = self.client.get(reverse('shop:list_category', args=['books']), data={'to': 50})
        self.assertNotContains(response, 'Django 3')
        self.assertContains(response, 'Peak')
    
    def test_account(self):
        response = self.user.get(reverse('shop:account'))

        self.assertEqual(response.status_code, 200)
        
    # def test_login(self):
    #     response = self.client.post(reverse('shop:login'), data={'username': 'aleo', 'password': 'aleoaleo'})
    #     self.assertEqual(response.status_code, 302)
        
