import datetime as d
from decimal import Decimal
import pytz

from django.test import TestCase

from coupon.models import Coupon

class ModelTestCase(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(code='1234abc', discount=0.30 , valid_from=d.datetime(2021, 11, 24, tzinfo=pytz.UTC), valid_to=(d.datetime(2021, 11, 24, tzinfo=pytz.UTC) + d.timedelta(days=5)), active=True)
    
    def test_coupon(self):
        self.assertEqual(self.coupon.discount, Decimal(0.30))