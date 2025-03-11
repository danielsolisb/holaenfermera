from django.contrib import admin
from .models import Manufacturer, Medication, MedicationLot

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'medication_type', 'manufacturer', 'route_of_administration', 
                   'form_of_sale', 'stock', 'price']
    list_filter = ['medication_type', 'manufacturer', 'route_of_administration', 'form_of_sale']
    search_fields = ['name', 'manufacturer__name']
    list_editable = ['stock', 'price']
    ordering = ['name']

@admin.register(MedicationLot)
class MedicationLotAdmin(admin.ModelAdmin):
    list_display = ['medication', 'lot_number', 'expiration_date', 'quantity', 'storage_conditions']
    list_filter = ['medication', 'expiration_date']
    search_fields = ['medication__name', 'lot_number']
    list_editable = ['quantity', 'storage_conditions']
    ordering = ['expiration_date']
