from django.contrib import admin
from .models import TodoItem, Supplier, DeliveryRoute, EmissionData
# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Supplier)
admin.site.register(DeliveryRoute)
admin.site.register(EmissionData)

