from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name='order'),
    path('parcels/', views.ParcelView.as_view(), name='parcel'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
]
