from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pareto','nept_id', 'name', 'administration_type', 'sale_form', 'specialty', 'price')
    search_fields = ('pareto','nept_id', 'name', 'specialty')
