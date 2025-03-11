# store/models.py
from django.db import models
from CoreApps.common.models import Location

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    # Otros campos que consideres relevantes

    def __str__(self):
        return self.name

class Medication(models.Model):
    MEDICATION_TYPE_CHOICES = (
        ('drug', 'Medicamento'),
        ('vaccine', 'Vacuna'),
        ('suero', 'Suero'),
        # Puedes agregar más categorías si lo necesitas
    )
    name = models.CharField(max_length=255)
    medication_type = models.CharField(max_length=20, choices=MEDICATION_TYPE_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='medications')
    route_of_administration = models.CharField(max_length=50, help_text="Ej: Oral, Intramuscular, Endovenoso, etc.")
    form_of_sale = models.CharField(max_length=50, help_text="Ej: Bajo receta, OTC, etc.")
    # Para el control de stock (si manejas inventario básico):
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Otros campos que necesites (por ejemplo, concentración, número de registro sanitario, etc.)

    def __str__(self):
        return f"{self.name} - {self.get_medication_type_display()}"

class MedicationLot(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='lots')
    lot_number = models.CharField(max_length=50)
    expiration_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)
    storage_conditions = models.CharField(max_length=255, blank=True, null=True, help_text="Ej: mantener en frío")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='medication_lots', null=True, blank=True)
    def __str__(self):
        return f"Lote {self.lot_number} de {self.medication.name} (expira {self.expiration_date})"

#class Product(models.Model):
#    pareto = models.CharField(max_length=50, unique=False, verbose_name="Pareto")
#    nept_id = models.CharField(max_length=50, unique=True, verbose_name="ID Nept")
#    name = models.CharField(max_length=100, verbose_name="Nombre del producto")
#    administration_type = models.CharField(max_length=100, verbose_name="Tipo de administración")
#    sale_form = models.CharField(max_length=100, verbose_name="Forma de venta")
#    specialty = models.CharField(max_length=100, verbose_name="Especialidad")
#    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        verbose_name = "Product"
#        verbose_name_plural = "Products"

#class Vaccine(models.Model):
#    name = models.CharField(max_length=100, verbose_name="Nombre de la vacuna")
#    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
#    # Puedes agregar otros campos como fabricante, lote, etc.
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        verbose_name = "Vacuna"
#        verbose_name_plural = "Vacunas"
#
#
#class SuerotherapyProduct(models.Model):
#    name = models.CharField(max_length=100, verbose_name="Nombre del producto de sueroterapia")
#    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
#    # Puedes incluir otros campos específicos para sueroterapia.
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        verbose_name = "Producto de sueroterapia"
#        verbose_name_plural = "Productos de sueroterapia"
