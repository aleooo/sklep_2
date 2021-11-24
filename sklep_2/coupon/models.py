from django.db import models
from django.db.models.base import Model


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(decimal_places=2, max_digits=3)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()

    

