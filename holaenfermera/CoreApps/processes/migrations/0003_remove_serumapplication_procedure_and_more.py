# Generated by Django 4.2.4 on 2025-02-08 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_suerotherapyproduct_vaccine'),
        ('processes', '0002_doctor_suerotherapyapplication_next_application_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serumapplication',
            name='procedure',
        ),
        migrations.RemoveField(
            model_name='suerotherapyapplication',
            name='medicine_manual',
        ),
        migrations.RemoveField(
            model_name='suerotherapyapplication',
            name='suerotherapy',
        ),
        migrations.RemoveField(
            model_name='vaccineapplication',
            name='medicine_manual',
        ),
        migrations.RemoveField(
            model_name='vaccineapplication',
            name='vaccine',
        ),
        migrations.AddField(
            model_name='serumapplication',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio del Servicio'),
        ),
        migrations.AddField(
            model_name='suerotherapyapplication',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='vaccineapplication',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='suerotherapyapplication',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Final'),
        ),
        migrations.AlterField(
            model_name='vaccineapplication',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio Final'),
        ),
        migrations.CreateModel(
            name='ServiceFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('vaccine', 'Aplicación de vacuna'), ('suerotherapy', 'Aplicación de sueroterapia'), ('serum', 'Aplicación de suero')], max_length=20, verbose_name='Tipo de Servicio')),
                ('location', models.CharField(choices=[('local', 'En el local'), ('domicile', 'A domicilio')], max_length=20, verbose_name='Ubicación')),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tarifa')),
            ],
            options={
                'verbose_name': 'Tarifa de Servicio',
                'verbose_name_plural': 'Tarifas de Servicio',
                'unique_together': {('service_type', 'location')},
            },
        ),
    ]
