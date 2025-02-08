from django.contrib import admin

# Register your models here.
from .models import (
    Consent,
    Prescription,
    SerumApplication,
    VaccineApplication,
    SuerotherapyApplication,
    Doctor,
    ServiceFee
)
@admin.register(SerumApplication)
class SerumApplicationAdmin(admin.ModelAdmin):
    # Ahora ya no se usa 'procedure' ya que se eliminó; mostramos 'product' y 'price'
    list_display = ('id', 'patient', 'product', 'price', 'location', 'date_time')
    list_filter = ('location',)

@admin.register(VaccineApplication)
class VaccineApplicationAdmin(admin.ModelAdmin):
    # En lugar de 'vaccine', se usa 'product'
    list_display = ('id', 'patient', 'product', 'price', 'next_application', 'location', 'date_time')
    list_filter = ('location',)

@admin.register(SuerotherapyApplication)
class SuerotherapyApplicationAdmin(admin.ModelAdmin):
    # En lugar de 'suerotherapy', se usa 'product'
    list_display = ('id', 'patient', 'product', 'price', 'next_application', 'location', 'date_time')
    list_filter = ('location',)

@admin.register(ServiceFee)
class ServiceFeeAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'location', 'fee')
    list_filter = ('service_type', 'location')

# Puedes registrar también los modelos de documentos y Doctor:
@admin.register(Consent)
class ConsentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'age', 'document_date')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'prescription_date')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialty')