# services/models.py
from django.db import models
from django.conf import settings

from CoreApps.store.models import Medication
from CoreApps.common.models import Location, OrderLocation


class ServiceAppointment(models.Model):
    SERVICE_TYPE_CHOICES = (
        ('inyeccion', 'Inyección'),
        ('med_especialidad', 'Aplicación de Medicamento de Especialidad'),
        ('suero', 'Aplicación de Suero'),
        ('sueroterapia', 'Sueroterapia'),
        ('vacunacion', 'Vacunación'),
        ('guardias', 'Guardias'),
        ('otros', 'Otros procedimientos'),
        # ...
    )
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('completed', 'Completada'),
        ('canceled', 'Cancelada'),
    )
    PLACE_TYPE_CHOICES = (
        ('branch', 'Sucursal'),
        ('domicile', 'Domicilio'),
    )
    
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments',
        limit_choices_to={'user_type': 'client'}
    )
    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_appointments',
        limit_choices_to={'user_type': 'nurse'}
    )
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # Nuevo campo para indicar el tipo de ubicación elegida
    service_place_type = models.CharField(max_length=20, choices=PLACE_TYPE_CHOICES, default='branch')
    # Ubicación para sucursal
    branch = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments_branch',
        help_text="Sucursal donde se realizará el servicio (si aplica)"
    )
    # Ubicación para domicilio
    order_location = models.ForeignKey(
        OrderLocation,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments_domicile',
        help_text="Dirección a domicilio para el servicio (si aplica)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        # Según el tipo de ubicación seleccionado, se debe rellenar solo un campo
        if self.service_place_type == 'branch':
            if not self.branch:
                raise ValidationError("Debes seleccionar una sucursal para el servicio.")
            if self.order_location:
                raise ValidationError("Para una sucursal, no se debe ingresar dirección de domicilio.")
        elif self.service_place_type == 'domicile':
            if not self.order_location:
                raise ValidationError("Debes seleccionar la dirección de domicilio para el servicio.")
            if self.branch:
                raise ValidationError("Para domicilio, no se debe seleccionar una sucursal.")
        else:
            raise ValidationError("El tipo de ubicación es requerido.")
        super().clean()

    def __str__(self):
        return f"{self.get_service_type_display()} para {self.patient.email} el {self.appointment_date}"

#class ServiceAppointment(models.Model):
#    SERVICE_TYPE_CHOICES = (
#        ('inyeccion', 'Inyección'),
#        ('med_especialidad', 'Aplicación de Medicamento de Especialidad'),
#        ('suero', 'Aplicación de Suero'),
#        ('sueroterapia', 'Sueroterapia'),
#        ('vacunacion', 'Vacunación'),
#        ('guardias', 'Guardias'),
#        ('otros', 'Otros procedimientos'),
#        # ...
#    )
#
#    STATUS_CHOICES = (
#        ('pending', 'Pendiente'),
#        ('confirmed', 'Confirmada'),
#        ('completed', 'Completada'),
#        ('canceled', 'Cancelada'),
#    )
#
#    patient = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#        related_name='appointments',
#        limit_choices_to={'user_type': 'client'}
#    )
#    nurse = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#        related_name='assigned_appointments',
#        limit_choices_to={'user_type': 'nurse'}
#    )
#    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
#    appointment_date = models.DateTimeField()
#    location = models.CharField(max_length=255, help_text="Dirección o local de atención")
#    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#
#    def __str__(self):
#        return f"{self.get_service_type_display()} para {self.patient.email} el {self.appointment_date}"

class MedicalDetail(models.Model):
    appointment = models.OneToOneField(ServiceAppointment, on_delete=models.CASCADE, related_name='medical_detail')
    has_prescription = models.BooleanField(default=False)
    prescription_file = models.FileField(upload_to='prescriptions/', blank=True, null=True)
    consent_file = models.FileField(upload_to='consents/', blank=True, null=True)
    consent_given = models.BooleanField(default=False)

    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    doctor_license = models.CharField(max_length=50, blank=True, null=True)

    def clean(self):
        # Requerimientos según el tipo de servicio
        service_type = self.appointment.service_type

        if service_type in ['inyeccion', 'suero']:
            # Necesita receta o consentimiento
            if not self.has_prescription and not self.consent_given:
                raise ValidationError("Se requiere receta o consentimiento para este servicio.")
            # Opcional: si quieres forzar que suban el PDF
            if not self.prescription_file and not self.consent_file:
                raise ValidationError("Debes adjuntar al menos uno: receta o consentimiento.")
        
        elif service_type in ['vacunacion', 'sueroterapia']:
            # Necesita consentimiento
            if not self.consent_given:
                raise ValidationError("Se requiere consentimiento para este servicio.")
            # Opcional: si quieres forzar el PDF
            if not self.consent_file:
                raise ValidationError("Debes adjuntar el PDF de consentimiento.")

        super().clean()

    def __str__(self):
        return f"Detalle médico de la cita {self.appointment.id}"


#class MedicalDetail(models.Model):
#    appointment = models.OneToOneField(
#        ServiceAppointment,
#        on_delete=models.CASCADE,
#        related_name='medical_detail'
#    )
#    has_prescription = models.BooleanField(default=False)
#    doctor_name = models.CharField(max_length=255, blank=True, null=True)
#    doctor_license = models.CharField(max_length=50, blank=True, null=True)
#    consent_given = models.BooleanField(default=False, help_text="Consentimiento informado")
#
#    def __str__(self):
#        return f"Detalle médico de la cita {self.appointment.id}"


class MedicationAdministration(models.Model):
    appointment = models.ForeignKey(ServiceAppointment, on_delete=models.CASCADE, related_name='medications_administered')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='administrations')
    dosage = models.CharField(max_length=50, help_text="Dosis aplicada, ej: 5ml, 1 ampolla")
    administration_time = models.DateTimeField(auto_now_add=True)
    # Si deseas registrar quién lo administró, ya está en la cita (nurse), pero puedes duplicar si deseas
    administered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'user_type': 'nurse'}
    )

    def __str__(self):
        return f"{self.medication.name} - {self.dosage} en la cita {self.appointment.id}"
