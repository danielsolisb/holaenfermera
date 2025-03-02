# Generated by Django 4.2.4 on 2025-02-08 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Doctor')),
                ('specialty', models.CharField(blank=True, max_length=100, null=True, verbose_name='Especialidad')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.AddField(
            model_name='suerotherapyapplication',
            name='next_application',
            field=models.DateField(blank=True, null=True, verbose_name='Próxima Aplicación'),
        ),
        migrations.AddField(
            model_name='vaccineapplication',
            name='next_application',
            field=models.DateField(blank=True, null=True, verbose_name='Próxima Aplicación'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processes.doctor', verbose_name='Doctor'),
        ),
    ]
