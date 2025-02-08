# models.py (en la app processes, por ejemplo)

from django.db import models
from django.core.exceptions import ValidationError
from CoreApps.patients.models import Patient
from CoreApps.store.models import Vaccine
from CoreApps.store.models import SuerotherapyProduct
from CoreApps.store.models import Product 
#from .models import Doctor
from django.utils.timezone import now


class Consent(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    age = models.PositiveIntegerField(verbose_name="Edad")
    document_date = models.DateField(auto_now_add=True, verbose_name="Fecha del Documento")
    signature = models.ImageField(upload_to='consents/', verbose_name="Firma del Consentimiento")
    
    def __str__(self):
        return f"Consentimiento de {self.patient.first_names} {self.patient.last_names}"

    class Meta:
        verbose_name = "Consentimiento"
        verbose_name_plural = "Consentimientos"


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Doctor")
    prescription_date = models.DateField(auto_now_add=True, verbose_name="Fecha de la Receta")
    pdf = models.FileField(upload_to='prescriptions/', verbose_name="PDF de la Receta")
    
    def __str__(self):
        return f"Receta de {self.patient.first_names} {self.patient.last_names}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"


class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Doctor")
    specialty = models.CharField(max_length=100, null=True, blank=True, verbose_name="Especialidad")
    phone       = models.CharField(max_length=20, null=True, blank=True, verbose_name="Teléfono")
    email       = models.EmailField(unique=True, null=True, blank=True, verbose_name="Correo")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"


#Modelo padre para los servicios

class AbstractService(models.Model):
    LOCATION_CHOICES = (
        ('domicile', 'A domicilio'),
        ('local', 'En el local'),
    )

    #patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="services", verbose_name="Paciente")
    patient = models.ForeignKey(
        Patient, 
        on_delete=models.CASCADE, 
        related_name="%(class)ss",  # Usamos %(class)s para que sea único para cada modelo hijo
        verbose_name="Paciente"
    )
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora")
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, verbose_name="Ubicación")
    
    # Cada servicio debe tener un único documento, ya sea receta o consentimiento.
    prescription = models.OneToOneField(
        'Prescription',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Receta"
    )
    consent = models.OneToOneField(
        'Consent',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Consentimiento"
    )

    class Meta:
        abstract = True

    def clean(self):
        # Valida que se asigne exactamente un documento (receta o consentimiento).
        if (self.prescription and self.consent) or (not self.prescription and not self.consent):
            raise ValidationError("Debe asignarse exactamente un documento: receta o consentimiento.")

    def __str__(self):
        return f"Servicio para {self.patient}"


# Servicio: Aplicación de Suero (usa el modelo Product de store)

class SerumApplication(AbstractService):
    PROCEDURE_CHOICES = (
        ('colocado', 'Colocado únicamente'),
        ('colocado_retirado', 'Colocado y retirado'),
    )
    procedure = models.CharField(max_length=30, choices=PROCEDURE_CHOICES, verbose_name="Procedimiento")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Producto")

    def __str__(self):
        return f"Aplicación de suero ({self.get_procedure_display()}) para {self.patient}"

    class Meta:
        verbose_name = "Aplicación de suero"
        verbose_name_plural = "Aplicaciones de suero"


# Servicio: Aplicación de Vacunas (usa el modelo Vaccine de store)

class VaccineApplication(AbstractService):
    # Aquí ya no se definen opciones fijas; se selecciona el producto de la tabla Vaccine.
    vaccine = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Vacuna")
    
    # Si se requiere también la opción de ingresar manualmente el medicamento y precio, se pueden mantener:
    medicine_manual = models.CharField(max_length=255, null=True, blank=True, verbose_name="Medicamento (manual)")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio")
    next_application = models.DateField(null=True, blank=True, verbose_name="Próxima Aplicación")

    def save(self, *args, **kwargs):
        # Si se selecciona una vacuna, copia el precio de ese producto
        if self.vaccine:
            self.price = self.vaccine.price
        super(VaccineApplication, self).save(*args, **kwargs)

    def clean(self):
        # Primero se ejecuta la validación del modelo abstracto
        super().clean()
        # Si se ha asignado un consentimiento, verificar que no esté usado en otro servicio
        if self.consent:
            from .models import SerumApplication, VaccineApplication, SuerotherapyApplication
            qs_serum = SerumApplication.objects.filter(consent=self.consent)
            qs_vaccine = VaccineApplication.objects.filter(consent=self.consent)
            qs_suerotherapy = SuerotherapyApplication.objects.filter(consent=self.consent)
            
            # Excluir el servicio actual si ya existe (en caso de actualización)
            if self.pk:
                qs_serum = qs_serum.exclude(pk=self.pk)
                qs_vaccine = qs_vaccine.exclude(pk=self.pk)
                qs_suerotherapy = qs_suerotherapy.exclude(pk=self.pk)
            
            if qs_serum.exists() or qs_vaccine.exists() or qs_suerotherapy.exists():
                raise ValidationError("Este consentimiento ya está asociado a otro servicio.")
    

    def __str__(self):
        return f"Aplicación de vacuna para {self.patient}"

    class Meta:
        verbose_name = "Aplicación de vacuna"
        verbose_name_plural = "Aplicaciones de vacunas"


# Servicio: Aplicación de Sueroterapia (usa el modelo SuerotherapyProduct de store)

class SuerotherapyApplication(AbstractService):
    suerotherapy = models.ForeignKey(SuerotherapyProduct, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Producto de sueroterapia")
    
    medicine_manual = models.CharField(max_length=255, null=True, blank=True, verbose_name="Medicamento (manual)")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio")
    next_application = models.DateField(null=True, blank=True, verbose_name="Próxima Aplicación")
    
    def save(self, *args, **kwargs):
        # Si se selecciona un producto de sueroterapia, se copia su precio
        if self.suerotherapy:
            self.price = self.suerotherapy.price
        super(SuerotherapyApplication, self).save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.consent:
            from .models import SerumApplication, VaccineApplication, SuerotherapyApplication
            qs_serum = SerumApplication.objects.filter(consent=self.consent)
            qs_vaccine = VaccineApplication.objects.filter(consent=self.consent)
            qs_suerotherapy = SuerotherapyApplication.objects.filter(consent=self.consent)
            
            if self.pk:
                qs_serum = qs_serum.exclude(pk=self.pk)
                qs_vaccine = qs_vaccine.exclude(pk=self.pk)
                qs_suerotherapy = qs_suerotherapy.exclude(pk=self.pk)
            
            if qs_serum.exists() or qs_vaccine.exists() or qs_suerotherapy.exists():
                raise ValidationError("Este consentimiento ya está asociado a otro servicio.")

    def __str__(self):
        return f"Aplicación de sueroterapia para {self.patient}"

    class Meta:
        verbose_name = "Aplicación de sueroterapia"
        verbose_name_plural = "Aplicaciones de sueroterapia"