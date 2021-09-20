from django.db import models
from django.db.models.query_utils import select_related_descend


def get_path_upload_to(instance):
    return f'products/{instance.name}/{instance.id}'


class Products(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to=get_path_upload_to)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity_available = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.available}'

    





 
        
