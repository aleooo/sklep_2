from django.test import TestCase
from django.contrib.auth.models import User

from shop.models import Products, Category, UserModel, Address


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
        address = Address.objects.create(street='Krotka', street_number='3', ZIP_code='08-116', town='Seroczyn', country='Poland')
        UserModel.objects.create(username='aleo', first_name='alek', last_name='wiedenski', email='dwdawdw@gmail.com', password='aleoaleo', address=address, number=333333333)
                                
    def test_model_Category(self):
        category = Category.objects.first()
        self.assertEqual(category.name, 'Books')

    def test_model_Product(self):
        products = Products.objects.all()
        self.assertEqual(len(products), 2)
    
    def test_model_Address(self):
        address = Address.objects.first()
        self.assertEqual(address.street, 'Krotka')

    def test_model_UserModel(self):
        user = UserModel.objects.first()
        self.assertEqual(user.number, 333333333)
    
