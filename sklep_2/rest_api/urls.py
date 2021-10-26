from django.urls import path, include

from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'addresses', views.AddressViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.UserModelViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-products', views.OrderProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]