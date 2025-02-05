from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_names', 'last_names', 'id_card', 'email', 'phone', 'birth_date')
    search_fields = ('first_names', 'last_names', 'id_card', 'email')

# También puedes usar:
# admin.site.register(Patient, PatientAdmin)
