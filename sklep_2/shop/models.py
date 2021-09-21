from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


def get_path_upload_to(instance):
    return f'products/{instance.name}/{instance.id}'


class Address(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    ZIP_code = models.CharField(max_length=15)
    town = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class UserModel(AbstractUser):
    address = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True)
    number = models.IntegerField(validators=[MaxLengthValidator(9), MinLengthValidator(9)])

    class Meta:
        ordering = ('-last_name', '-first_name')
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.id}'
    


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    
class Products(models.Model):
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

    def __str__(self):
        return f'{self.name} {self.price} {self.available}'

    





 
        
