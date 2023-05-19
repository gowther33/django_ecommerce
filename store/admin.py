from django.contrib import admin
from .models import *


# Registering the models shows them on the admin site
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)