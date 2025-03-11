# users/models.py
from holaenfermera.settings import MEDIA_ROOT, BASE_DIR, STATIC_URL, MEDIA_URL
from django.db import models
from django.conf import settings

from django.db.models.fields import EmailField
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
from django.db.models.query import FlatValuesListIterable
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.fields.files import ImageField
from CoreApps.common.models import Location


import datetime



class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email debe ser proporcionado")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # Opcional: asignar un user_type específico para superusuarios
        extra_fields.setdefault('user_type', 'system_admin')
        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True")
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    # Eliminamos el campo username
    username = None
    email = models.EmailField(unique=True)
    identification_number = models.CharField( 
    max_length=20,
    unique=True,
    null=True,
    blank=True,
    help_text="Cédula o identificación personal")
    USER_TYPE_CHOICES = (
        ('system_admin', 'Administrador del sistema'),
        ('nurse', 'Enfermero'),
        ('seller', 'Vendedor'),
        ('account_admin', 'Administrador contable'),
        ('client', 'Cliente'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Asignamos el manager personalizado
    objects = CustomUserManager()

    # Indicamos que email es el identificador principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Agrega otros campos requeridos si es necesario

    def save(self, *args, **kwargs):
        if self.user_type == 'system_admin':
            self.is_staff = True  # Superadministradores tienen acceso al admin
        elif self.user_type == 'client':
            self.is_staff = False  # Siempre se fuerza a False para clientes
        # Puedes agregar lógica para otros roles según sea necesario.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_user_login(self):
        return str(self.pk)


# Modelo para Localidades/Sucursales
#class Location(models.Model):
#    name = models.CharField(max_length=100, unique=True, help_text="Nombre de la localidad o sucursal")
#    address = models.CharField(max_length=255, help_text="Dirección completa de la localidad")
#    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Teléfono de contacto")
#    email = models.EmailField(blank=True, null=True, help_text="Correo electrónico de contacto")
#    is_active = models.BooleanField(default=True, help_text="Indica si la localidad está activa")
#    
#    def __str__(self):
#        return self.name
#    
#    class Meta:
#        verbose_name = "Localidad"
#        verbose_name_plural = "Localidades"


# Modelo para Especialidades en enfermería
class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Nombre de la especialidad")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"


class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nurse_profile')
    license_number = models.CharField(max_length=50, help_text="Número de licencia profesional")
    # Se utiliza ManyToMany para elegir de un conjunto predefinido de especialidades
    specialties = models.ManyToManyField(Specialty, blank=True, help_text="Especialidades en enfermería")
    available = models.BooleanField(default=True, help_text="Indica disponibilidad para atender")
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, help_text="Valoración (0.00 a 5.00)")
    # Nuevos campos para la asignación de localidad o trabajo online
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='nurses', help_text="Localidad asignada para trabajo")
    is_online_worker = models.BooleanField(default=False, help_text="Indica si trabaja en modalidad online")
    
    def __str__(self):
        return f"Enfermero: {self.user.email}"
    
    def save(self, *args, **kwargs):
        # Si tiene localidad asignada, no puede ser trabajador online y viceversa
        if self.location is not None:
            self.is_online_worker = False
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Perfil de Enfermero"
        verbose_name_plural = "Perfiles de Enfermeros"


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    # El vendedor registra ventas para la plataforma, asignado a una zona o región
    sales_region = models.CharField(max_length=100, help_text="Zona o región asignada para ventas")
    employee_id = models.CharField(max_length=50, blank=True, null=True, help_text="Identificador de empleado")
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, help_text="Valoración del desempeño")
    # Nuevos campos para la asignación de localidad o trabajo online
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='sellers', help_text="Localidad asignada para trabajo")
    is_online_worker = models.BooleanField(default=False, help_text="Indica si trabaja en modalidad online")
    
    def __str__(self):
        return f"Vendedor: {self.user.email}"
    
    def save(self, *args, **kwargs):
        # Si tiene localidad asignada, no puede ser trabajador online y viceversa
        if self.location is not None:
            self.is_online_worker = False
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Perfil de Vendedor"
        verbose_name_plural = "Perfiles de Vendedores"


class AccountAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account_admin_profile')
    department = models.CharField(max_length=100, help_text="Departamento o área de trabajo")
    employee_id = models.CharField(max_length=50, unique=True, help_text="Identificador único de empleado")
    
    def __str__(self):
        return f"Administrador Contable: {self.user.email}"
    
    class Meta:
        verbose_name = "Perfil de Administrador Contable"
        verbose_name_plural = "Perfiles de Administradores Contables"


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    address = models.CharField(max_length=255, help_text="Dirección completa")
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Teléfono de contacto")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Fecha de nacimiento")
    MEDICAL_INSURANCE_CHOICES = (
        ('iess', 'IESS'),
        ('private', 'Seguro Privado'),
        ('none', 'Ninguno'),
    )
    medical_insurance = models.CharField(max_length=10, choices=MEDICAL_INSURANCE_CHOICES, default='none', help_text="Tipo de seguro médico")
    
    def __str__(self):
        return f"Cliente: {self.user.email}"
    
    class Meta:
        verbose_name = "Perfil de Cliente"
        verbose_name_plural = "Perfiles de Clientes"
    
    
#class Availability(models.Model):
#    WEEKDAY_CHOICES = (
#        (0, 'Lunes'),
#        (1, 'Martes'),
#        (2, 'Miércoles'),
#        (3, 'Jueves'),
#        (4, 'Viernes'),
#        (5, 'Sábado'),
#        (6, 'Domingo'),
#    )
#    nurse = models.ForeignKey(
#        settings.AUTH_USER_MODEL,
#        on_delete=models.CASCADE,
#        limit_choices_to={'user_type': 'nurse'}
#    )
#    day_of_week = models.IntegerField(choices=WEEKDAY_CHOICES)
#    start_time = models.TimeField()
#    end_time = models.TimeField()
#
#    def __str__(self):
#        return f"{self.nurse.email} - {self.get_day_of_week_display()} {self.start_time} - {self.end_time}"

class Availability(models.Model):
    WEEKDAY_CHOICES = (
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'nurse'}
    )
    day_of_week = models.IntegerField(choices=WEEKDAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.nurse.email} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"

class HolidayException(models.Model):
    nurse = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'nurse'}
    )
    date = models.DateField(help_text="Día festivo o excepción")
    is_off = models.BooleanField(default=True, help_text="Si está libre este día entero")
    # Opcional: si el enfermero trabaja parcialmente, se pueden agregar campos de horario
    # start_time = models.TimeField(null=True, blank=True)
    # end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Excepción de {self.nurse.email} en {self.date}"
