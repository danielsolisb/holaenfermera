# Generated by Django 4.2.4 on 2025-02-07 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='pareto',
            field=models.CharField(default=1, max_length=50, verbose_name='Pareto'),
            preserve_default=False,
        ),
    ]
