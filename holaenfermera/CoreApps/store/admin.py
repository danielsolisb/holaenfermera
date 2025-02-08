from django.contrib import admin
from .models import Product, Vaccine, SuerotherapyProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pareto','nept_id', 'name', 'administration_type', 'sale_form', 'specialty', 'price')
    search_fields = ('pareto','nept_id', 'name', 'specialty')

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')

@admin.register(SuerotherapyProduct)
class SuerotherapyProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')