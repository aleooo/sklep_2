from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('added/<str:id>/', views.add_to_cart, name='add'),
    path('remove/<str:id>/', views.RemoveItem.as_view(), name='remove_item'),
    path('', views.MainCart.as_view(), name='main_cart'),
]
