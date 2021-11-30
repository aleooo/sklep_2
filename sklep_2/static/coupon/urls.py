from django.urls import path

from coupon import views


app_name = 'coupon'

urlpatterns = [
    path('coupon/', views.coupon, name='coupon')
]
