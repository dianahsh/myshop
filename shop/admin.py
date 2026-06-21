from django.contrib import admin
from .models import Product, Category, ShoppingCart, Order, ShoppinList, OrderList
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(ShoppinList)
admin.site.register(OrderList)