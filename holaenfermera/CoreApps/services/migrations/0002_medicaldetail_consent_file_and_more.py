# Generated by Django 4.2.4 on 2025-03-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaldetail',
            name='consent_file',
            field=models.FileField(blank=True, null=True, upload_to='consents/'),
        ),
        migrations.AddField(
            model_name='medicaldetail',
            name='prescription_file',
            field=models.FileField(blank=True, null=True, upload_to='prescriptions/'),
        ),
        migrations.AlterField(
            model_name='medicaldetail',
            name='consent_given',
            field=models.BooleanField(default=False),
        ),
    ]
