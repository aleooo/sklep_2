
from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB,
                      charset='UTF-8',
                      decode_responses=True)

# This class is used for product recommendations
class Recommender(object):
    def get_popular_products(self):
        products = r.zrange('purchased_product_key', 0, -1, desc=True, withscores=True, byscore=False)[:8]
        return products

    def suggestion_product_key(self, id):
        return f'product:{id}:purchased_with'
    
    def purchased_product_key(self, id):
        return f'product:{id}:purchased'

    # the method adds to redis database purchased products with quantity
    # and if order has greater than one product, the method creates in redis database
    # key of id product and value. Products data is placed in the value.
    # This is used to make product suggestions when we buy something  
    def products_bought(self, products):
        products_ids = [p.id for p in products.keys()]
        for product_id in products_ids:
            r.zincrby('purchased_product_key', amount=products[product_id], value=product_id)
            for with_product in products_ids:
                if product_id != with_product:
                    r.zincrby(self.suggestion_product_key(product_id), amount=products[with_product], value=with_product)

    
