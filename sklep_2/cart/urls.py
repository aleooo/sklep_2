from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('<int:id>/added/', views.add_to_cart, name='add'),
    path('<str:id>/remove/', views.remove_item, name='remove_item'),
    path('', views.main_cart, name='main_cart'),
]
