# Generated by Django 5.1.5 on 2025-03-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geraete', '0007_remove_geraet_feueron'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geraet',
            name='barcode',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
