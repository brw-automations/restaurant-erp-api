from django.contrib import admin
from core.models.Product import Product
from core.models.Category import Category
from core.models.Order import Order
from core.models.OrderItem import OrderItem
from core.models.table import Table

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Table)
