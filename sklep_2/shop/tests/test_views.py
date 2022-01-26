from django.http import response
from django.http.request import HttpRequest
from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls.base import resolve, reverse

from shop.models import Address, Category, Product, UserModel
from shop.views import  register
from shop.utils import filter_prices_products



class ShopViewTest(TestCase):
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
        self.user = UserModel.objects.create(username='aleo', first_name='alek', last_name='wiedenski', email='dwdawdw@gmail.com', password='aleoaleo', address=address, number='+48510865704')
        self.user_without_data = UserModel.objects.create(username='alek', password='aleoaleo')
        
        
    
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
    
    def test_search_with_available_letter(self):
        response = self.client.post(reverse('shop:search'), data={'text': 'a'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Django')
        self.assertContains(response, 'Peak')
    
    def test_search_with_not_available_letter(self):
        response = self.client.post(reverse('shop:search'), data={'text': 'x'})

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'data': []})

    def test_detail(self):
        product = Product.objects.first()
        response = self.client.get(product.get_absolute_url())  
        self.assertContains(response, 'Peak')
    
    def test_list_none_input_search(self):
        response = self.client.get(reverse('shop:list'))
        
    def test_list_Category(self):
        response = self.client.get(reverse('shop:list_category', args=['books']))
        self.assertContains(response, 'Django 3')
    
    def test_list_filter_prices_products(self):
        response = self.client.get(reverse('shop:list_category', args=['books']), data={'filter': 'manual','to': 50})
        self.assertNotContains(response, 'Django 3')
        self.assertContains(response, 'Peak')
    
    def test_list_filter_equal_to_and_from_1(self):
        response = self.client.get(reverse('shop:list_category', args=['books']), data={'filter': 'manual', 'from': 50, 'to': 50})
        self.assertNotContains(response, 'Peak')
        self.assertNotContains(response, 'Django 3')
    
    def test_list_filter_equal_to_and_from_2(self):
        response = self.client.get(reverse('shop:list_category', args=['books']), data={'filter': 'manual', 'from': 49.99, 'to': 49.99})
        self.assertContains(response, 'Peak')
        self.assertNotContains(response, 'Django 3')
    
    def test_filter_prices_products_1(self):
        request = HttpRequest()
        data = {'filter': 'manual', 'from': '60', 'to': '1'}
        products = Product.objects.all()
        response = filter_prices_products(data, products)

        self.assertEqual(len(response), 1)
    
    def test_filter_prices_products_2(self):
        request = HttpRequest()
        data = {'filter': 'manual', 'from': '10', 'to': '0'}
        products = Product.objects.all()
        response = filter_prices_products(data, products)

        self.assertEqual(len(response), 2)

    def test_account_login_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:account'))
        self.assertEqual(response.status_code, 200)
    
    def test_account_logout_user(self):
        response = self.client.get(reverse('shop:account'))
        self.assertEqual(response.status_code, 302)
    
    def test_account_with_all_fill_fields(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'dwdawdw@gmail.com')
        self.assertContains(response, '-----')
    
    def test_account_without_data_user(self):
        self.client.force_login(self.user_without_data)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, '-----')
    
    def test_account_address(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'Seroczyn')
        self.assertContains(response, 'Poland')
        self.assertContains(response, 'Krotka')
        self.assertContains(response, '3')
        self.assertContains(response, '08-116')
    
    def test_account_personal_data(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'alek')
        self.assertContains(response, 'wiedenski')
        self.assertContains(response, 'dwdawdw@gmail.com')
        self.assertContains(response, '+48510865704')
    
    def test_account_data_form_address_one_field(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('shop:account_data', args=['address']), data={'town': 'Zaliczeniec', 'csrfmiddlewaretoken': 'awdawd1212@e4'})

        self.assertRedirects(response, expected_url=reverse('shop:account'), status_code=302, target_status_code=200)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'Zaliczeniec')
    
    def test_account_data_form_address_all_fields(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('shop:account_data', args=['address']), data={'town': 'Zaliczeniec', 'country': 'Poland',
                                                                                          'street': 'Oblique', 'street': '3',
                                                                                          'ZIP_code': '08-116', 'csrfmiddlewaretoken': 'awdawd1212@e4'})

        self.assertRedirects(response, expected_url=reverse('shop:account'), status_code=302, target_status_code=200)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'Zaliczeniec')
        self.assertContains(response, 'Poland')
        self.assertContains(response, '3')
        self.assertContains(response, '08-116')
    
    def test_account_data_form_personal_data_one_field(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('shop:account_data', args=['personal_data']), data={'number': '+48523765109',
                                                                                                'csrfmiddlewaretoken': 'dawdawdd211#21'})
        self.assertRedirects(response, expected_url=reverse('shop:account'), status_code=302, target_status_code=200)
        response = self.client.get(reverse('shop:account'))
        self.assertContains(response, '+48523765109')


    def test_account_data_form_personal_data_all_fields(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('shop:account_data', args=['personal_data']), data={'first_name': 'Trolo', 'last_name': 'Borek',
                                                                                                'email': 'trolo@gmail.com', 'number_0': '+48',
                                                                                                'number_1': '523765109', 
                                                                                                'csrfmiddlewaretoken': 'dawdawdd211#21'})
        
        self.assertRedirects(response, expected_url=reverse('shop:account'), status_code=302, target_status_code=200)
        response = self.client.get(reverse('shop:account'))

        self.assertContains(response, 'Trolo')
        self.assertContains(response, 'Borek')
        self.assertContains(response, 'trolo@gmail.com')
        self.assertContains(response, '+48523765109')
    
    

        



        
        
