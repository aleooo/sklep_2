from django.contrib import admin

from coupon.models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount' ,'valid_from', 'valid_to']
