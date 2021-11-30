import os

from django.urls import reverse

from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



def get_path_upload_to(self, filename):
    extension = filename.split('.')[-1]
    filename = f'{self.id}.{extension}'
    return os.path.join(f'products/', filename)


class Address(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    ZIP_code = models.CharField(max_length=15)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class UserModel(AbstractUser):
    address = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True)
    number = PhoneNumberField(blank=True, null=True)
    class Meta:
        ordering = ('-last_name', '-first_name')
        verbose_name = 'UserModel'
        verbose_name_plural = 'UserModels'
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.id}'
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to=get_path_upload_to, default='empty.png')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity_available = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Product'
        managed = True
        ordering = ['-id']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return f'{self.name}'
    

    def get_absolute_url(self):
        return reverse("shop:detail", args=[self.slug, 
                                       self.created.strftime('%S'), 
                                       self.created.strftime('%H'),
                                       self.id])
    

    

                                                                  

    





 
        
