# Generated by Django 4.2.4 on 2025-02-07 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_options_product_pareto'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuerotherapyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del producto de sueroterapia')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Producto de sueroterapia',
                'verbose_name_plural': 'Productos de sueroterapia',
            },
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la vacuna')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Vacuna',
                'verbose_name_plural': 'Vacunas',
            },
        ),
    ]
