from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Order, OrderProduct, Parcel


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('order:admin_order_pdf', args=[obj.id])))
order_pdf.short_description = 'Rachunek'


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'paid', 'created', 'updated', order_pdf]


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    pass
