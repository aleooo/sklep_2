from django.conf import settings
from django_fakeredis import FakeRedis
from django.test import TestCase
from django.test.client import Client
from django.urls.base import resolve, reverse
import redis
import fakeredis

from order.views import Recommender
from shop.models import Category, Product


class ShopRecommenderTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Books', slug='books')
        self.product_1 = Product.objects.create(category=category,
                                name='Django 3',
                                slug='django_3',
                                description='practical web application development',
                                price=69.99,
                                available=True,
                                quantity_available=13)
        self.product_2 = Product.objects.create(category=category,
                                name='Peak',
                                slug='peak',
                                description='Anyone who wants to get better at anything should read Peak',
                                price=49.99,
                                available=True,
                                quantity_available=4)
        self.data = {self.product_1.id: 3, self.product_2.id: 2}
        # fakeredis.FakeStrictRedis()
        self.r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB,
                      charset='UTF-8',
                      decode_responses=True)
        self.recommender = Recommender()

    # @FakeRedis("yourpath.get_redis_connection")
    # def test_products_bought(self):
    #     self.recommender.products_bought(self.data)
    #     products = self.r.zrange('purchased_product_key', 0, -1, desc=True, withscores=True, byscore=False)

    #     self.assertEqual(products, [])



        