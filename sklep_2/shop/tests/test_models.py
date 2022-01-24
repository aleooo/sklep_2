from django.test import TestCase
from django.contrib.auth.models import User

from shop.models import Product, Category, UserModel, Address


class ShopModelTest(TestCase):
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
                                
    def test_Category(self):
        category = Category.objects.first()
        self.assertEqual(category.name, 'Books')

    def test_Product(self):
        products = Product.objects.count()
        self.assertEqual(products, 2)
    
    def test_Address(self):
        address = Address.objects.first()
        self.assertEqual(address.street, 'Krotka')

    def test_UserModel(self):
        user = UserModel.objects.first()
        self.assertEqual(user.number, '333333333')
    
    def test_ProductG_get_absolute_url(self):
        product = Product.objects.first()
        seconds = product.created.strftime('%S')
        hours = product.created.strftime('%H')
        self.assertEqual(product.get_absolute_url(), f'/en/detail/{ product.slug }/{ seconds }/{ hours }/{ product.id }/')
    
