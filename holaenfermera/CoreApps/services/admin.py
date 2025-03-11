from django.contrib import admin
from .models import ServiceAppointment, MedicalDetail, MedicationAdministration

# Register your models here.
@admin.register(ServiceAppointment)
class ServiceAppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'nurse', 'service_type', 'appointment_date', 'service_place_type', 'status')
    list_filter = ('service_type', 'status', 'service_place_type')
    search_fields = ('patient__email', 'nurse__email', 'branch__name', 'order_location__address')
    date_hierarchy = 'appointment_date'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('branch', 'order_location')
        
    def get_search_results(self, request, queryset, search_term):
        """Personaliza la búsqueda para incluir ubicaciones relacionadas"""
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        return queryset, use_distinct

@admin.register(MedicalDetail)
class MedicalDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'has_prescription', 'consent_given', 'doctor_name', 'doctor_license')
    list_filter = ('has_prescription', 'consent_given')
    search_fields = ('doctor_name', 'doctor_license')
    fields = ('appointment', 'has_prescription', 'prescription_file', 'consent_given', 'consent_file', 'doctor_name', 'doctor_license')

@admin.register(MedicationAdministration)
class MedicationAdministrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'medication', 'dosage', 'administration_time', 'administered_by')
    list_filter = ('administration_time',)
    search_fields = ('medication__name', 'dosage')
    date_hierarchy = 'administration_time'
    #readonly_fields = ('prescription_file', 'consent_file')