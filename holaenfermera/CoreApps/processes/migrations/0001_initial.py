# Generated by Django 4.2.4 on 2025-02-07 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0003_suerotherapyproduct_vaccine'),
        ('patients', '0004_remove_patient_admins_patient_related_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField(verbose_name='Edad')),
                ('document_date', models.DateField(auto_now_add=True, verbose_name='Fecha del Documento')),
                ('signature', models.ImageField(upload_to='consents/', verbose_name='Firma del Consentimiento')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Consentimiento',
                'verbose_name_plural': 'Consentimientos',
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=100, verbose_name='Nombre del Doctor')),
                ('prescription_date', models.DateField(auto_now_add=True, verbose_name='Fecha de la Receta')),
                ('pdf', models.FileField(upload_to='prescriptions/', verbose_name='PDF de la Receta')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='VaccineApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('location', models.CharField(choices=[('domicile', 'A domicilio'), ('local', 'En el local')], max_length=20, verbose_name='Ubicación')),
                ('medicine_manual', models.CharField(blank=True, max_length=255, null=True, verbose_name='Medicamento (manual)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio')),
                ('consent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.consent', verbose_name='Consentimiento')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='patients.patient', verbose_name='Paciente')),
                ('prescription', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.prescription', verbose_name='Receta')),
                ('vaccine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.vaccine', verbose_name='Vacuna')),
            ],
            options={
                'verbose_name': 'Aplicación de vacuna',
                'verbose_name_plural': 'Aplicaciones de vacunas',
            },
        ),
        migrations.CreateModel(
            name='SuerotherapyApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('location', models.CharField(choices=[('domicile', 'A domicilio'), ('local', 'En el local')], max_length=20, verbose_name='Ubicación')),
                ('medicine_manual', models.CharField(blank=True, max_length=255, null=True, verbose_name='Medicamento (manual)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio')),
                ('consent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.consent', verbose_name='Consentimiento')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='patients.patient', verbose_name='Paciente')),
                ('prescription', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.prescription', verbose_name='Receta')),
                ('suerotherapy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.suerotherapyproduct', verbose_name='Producto de sueroterapia')),
            ],
            options={
                'verbose_name': 'Aplicación de sueroterapia',
                'verbose_name_plural': 'Aplicaciones de sueroterapia',
            },
        ),
        migrations.CreateModel(
            name='SerumApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora')),
                ('location', models.CharField(choices=[('domicile', 'A domicilio'), ('local', 'En el local')], max_length=20, verbose_name='Ubicación')),
                ('procedure', models.CharField(choices=[('colocado', 'Colocado únicamente'), ('colocado_retirado', 'Colocado y retirado')], max_length=30, verbose_name='Procedimiento')),
                ('consent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.consent', verbose_name='Consentimiento')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='patients.patient', verbose_name='Paciente')),
                ('prescription', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.prescription', verbose_name='Receta')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Aplicación de suero',
                'verbose_name_plural': 'Aplicaciones de suero',
            },
        ),
    ]
