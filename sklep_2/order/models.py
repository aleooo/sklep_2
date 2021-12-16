from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField

from shop.models import Product, UserModel

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = PhoneNumberField()
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    ZIP_code = models.CharField(max_length=15)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, related_name='order', on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{ self.last_name } { self.first_name }'
    
    def total_price(self):
        products = self.products.all()
        total = 0
        for product in products:
            total += product.total_price()
        return total



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{ str(self.id) } - { self.product.name }'
    
    def total_price(self):
        return self.quantity * self.product.price
    


    


