# Generated by Django 5.1.5 on 2025-03-10 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruefung', '0012_alter_monat_monat'),
    ]

    operations = [
        migrations.AddField(
            model_name='fahrzeug_pruefung',
            name='monat',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='pruefung.monat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fahrzeug_pruefung',
            name='datum',
            field=models.DateField(default='2025-02-25'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fahrzeug_pruefung',
            name='pruefer',
            field=models.CharField(max_length=50),
        ),
    ]
