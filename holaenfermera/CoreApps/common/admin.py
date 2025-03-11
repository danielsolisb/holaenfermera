from django.contrib import admin
from .models import Location, OrderLocation

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'email', 'location_type', 'is_active']
    list_filter = ['location_type', 'is_active']
    search_fields = ['name', 'address', 'email']
    list_editable = ['is_active']

@admin.register(OrderLocation)
class OrderLocationAdmin(admin.ModelAdmin):
    list_display = ['address', 'latitude', 'longitude']
    search_fields = ['address']
