from django.contrib import admin
from django.db import models

from .models import Category, Product, Address, UserModel

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username']
