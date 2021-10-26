from rest_framework import viewsets

from . import serializer
from shop.models import Address, Category, Product, UserModel
from order.models import Order, OrderProduct

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = serializer.AddressSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = serializer.UserModelSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer


class OrderProductViewSet(viewsets.ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = serializer.OrderProductSerializer
