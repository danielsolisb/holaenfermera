# Generated by Django 4.2.4 on 2025-03-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location_type',
            field=models.CharField(choices=[('branch', 'Sucursal'), ('home', 'Domicilio')], default='branch', max_length=20),
        ),
    ]
