from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('user', 'name','category','rating', 'numReviews', 'price', 'countInStock', 'createdAt', )
    list_per_page = 10
    list_filter =['category',]
@admin.register(Review)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
@admin.register(OrderItem)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
@admin.register(ShippingAddress)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10