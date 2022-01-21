from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category, Address
from cart.cart import Cart

class CartViewTest(TestCase):
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
        self.item = Product.objects.first()
        self.item_2 = Product.objects.last()
    def test_add_to_cart(self):
        response = self.client.get(reverse('cart:add', args=[self.item.id]), data={'quantity': 3})
        
        session = self.client.session
        self.assertEqual(session['cart'][str(self.item.id)]['name'], self.item.name)
        self.assertEqual(response.status_code, 302)
    
    def test_main_cart(self):
        response = self.client.get(reverse('cart:main_cart'))

        self.assertEqual(response.status_code, 200)
    
    def test_remove_item(self):
        self.client.get(reverse('cart:add', args=[str(self.item.id)]), data={'quantity': 3})
        session = self.client.session

        response = self.client.get(reverse('cart:remove_item', args=[self.item.id]))

        self.assertEqual(session['cart'], {})
        self.assertEqual(response.status_code, 302)
    
    def test_cart_iter(self):
        self.client.get(reverse('cart:add', args=[self.item.id]), data={'quantity': 3})
        session = self.client.session

        response = self.client.get(reverse('cart:main_cart'))
        self.assertContains(response, self.item.price)
    
    def test_cart_total_value_cart(self):
        self.client.get(reverse('cart:add', args=[self.item.id]), data={'quantity': 3})
        session = self.client.session
        response = self.client.get(reverse('cart:main_cart'))
        self.assertContains(response, str(3 * self.item.price)[-2:])

        

