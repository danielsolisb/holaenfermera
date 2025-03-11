# common/models.py
from django.db import models

class Location(models.Model):
    LOCATION_TYPE_CHOICES = (
        ('branch', 'Sucursal'),
        ('home', 'Domicilio'),
    )
    name = models.CharField(max_length=100, unique=True, help_text="Nombre de la ubicación o sucursal")
    address = models.CharField(max_length=255, help_text="Dirección completa de la ubicación")
    phone = models.CharField(max_length=15, blank=True, null=True, help_text="Teléfono de contacto")
    email = models.EmailField(blank=True, null=True, help_text="Correo electrónico de contacto")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES, default='branch')
    is_active = models.BooleanField(default=True, help_text="Indica si la ubicación está activa")
    
    def __str__(self):
        return self.name




class OrderLocation(models.Model):
    address = models.CharField(max_length=255, help_text="Dirección breve (puede ser autocompletada desde Google Maps)")
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    def __str__(self):
        return self.address
