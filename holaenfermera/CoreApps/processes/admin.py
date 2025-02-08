from django.contrib import admin

# Register your models here.
from .models import (
    Consent,
    Prescription,
    SerumApplication,
    VaccineApplication,
    SuerotherapyApplication,
    Doctor
)

@admin.register(Consent)
class ConsentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'age', 'document_date')
    search_fields = ('patient__first_names', 'patient__last_names')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'prescription_date')
    search_fields = ('patient__first_names', 'patient__last_names', 'doctor')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'phone', 'email')
    search_fields = ('name', 'specialty')

@admin.register(SerumApplication)
class SerumApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'procedure', 'location', 'date_time')
    search_fields = ('patient__first_names', 'patient__last_names')
    list_filter = ('procedure', 'location')

@admin.register(VaccineApplication)
class VaccineApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'vaccine', 'location', 'date_time', 'price')
    search_fields = ('patient__first_names', 'patient__last_names')
    list_filter = ('location',)

@admin.register(SuerotherapyApplication)
class SuerotherapyApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'suerotherapy', 'location', 'date_time', 'price')
    search_fields = ('patient__first_names', 'patient__last_names')
    list_filter = ('location',)