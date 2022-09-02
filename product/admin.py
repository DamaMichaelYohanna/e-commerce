from django.contrib import admin

from product.models import Store, Product, Preview, Category, Order, OrderItem

admin.site.register(Store)
admin.site.register(Preview)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

