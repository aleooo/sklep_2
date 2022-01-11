
from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB,
                      charset='UTF-8',
                      decode_responses=True)

class Recommender(object):
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'

    def products_bought(self, products):
        products_ids = [p.id for p in products.keys()]
        for product_id in products_ids:
            for with_product in products_ids:
                if product_id != with_product:
                    r.zincrby(self.get_product_key(product_id), amount=products[with_product], value=with_product)

    
