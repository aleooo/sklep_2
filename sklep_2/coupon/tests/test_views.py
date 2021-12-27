import datetime as d
import pytz
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from coupon.models import Coupon

class ViewTestCase(TestCase):
    def setUp(self):
        self.coupon = Coupon.objects.create(code='1234abc', discount=0.30 , valid_from=d.datetime(2021, 11, 24, tzinfo=pytz.UTC), valid_to=(d.datetime(2021, 11, 24, tzinfo=pytz.UTC) + d.timedelta(days=5)), active=True)
    
    def test_coupon(self):
        response = self.client.post(reverse('coupon:coupon'), data={'code': '1234abc'})

        self.assertEqual(response.status_code, 302)