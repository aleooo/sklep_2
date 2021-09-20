from django.db import models
from django.db.models.query_utils import select_related_descend


def get_path_upload_to(instance):
    return f'products/{instance.name}/{instance.id}'


class Products(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    image = models.ImageField(upload_to=get_path_upload_to)
    


 
        
