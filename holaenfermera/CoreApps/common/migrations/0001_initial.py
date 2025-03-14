# Generated by Django 4.2.4 on 2025-03-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de la ubicación o sucursal', max_length=100, unique=True)),
                ('address', models.CharField(help_text='Dirección completa de la ubicación', max_length=255)),
                ('phone', models.CharField(blank=True, help_text='Teléfono de contacto', max_length=15, null=True)),
                ('email', models.EmailField(blank=True, help_text='Correo electrónico de contacto', max_length=254, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('location_type', models.CharField(choices=[('branch', 'Sucursal'), ('home', 'Domicilio'), ('delivery', 'Punto de entrega')], default='branch', max_length=20)),
                ('is_active', models.BooleanField(default=True, help_text='Indica si la ubicación está activa')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(help_text='Dirección breve (puede ser autocompletada desde Google Maps)', max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
