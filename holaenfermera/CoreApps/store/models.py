from django.db import models

class Product(models.Model):
    pareto = models.CharField(max_length=50, unique=False, verbose_name="Pareto")
    nept_id = models.CharField(max_length=50, unique=True, verbose_name="ID Nept")
    name = models.CharField(max_length=100, verbose_name="Nombre del producto")
    administration_type = models.CharField(max_length=100, verbose_name="Tipo de administración")
    sale_form = models.CharField(max_length=100, verbose_name="Forma de venta")
    specialty = models.CharField(max_length=100, verbose_name="Especialidad")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Vaccine(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la vacuna")
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    # Puedes agregar otros campos como fabricante, lote, etc.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Vacuna"
        verbose_name_plural = "Vacunas"


class SuerotherapyProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del producto de sueroterapia")
    description = models.TextField(verbose_name="Descripción", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    # Puedes incluir otros campos específicos para sueroterapia.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto de sueroterapia"
        verbose_name_plural = "Productos de sueroterapia"
