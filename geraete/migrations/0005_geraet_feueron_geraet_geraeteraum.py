# Generated by Django 5.1.5 on 2025-03-08 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fahrzeuge', '0002_geraeteraum'),
        ('geraete', '0004_rename_katgorie_geraet_kategorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='geraet',
            name='feueron',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='geraet',
            name='geraeteraum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fahrzeuge.geraeteraum'),
        ),
    ]
