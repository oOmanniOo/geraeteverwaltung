# Generated by Django 5.1.5 on 2025-03-09 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruefung', '0011_fahrzeug_fragen_monat_fahrzeug_pruefung_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monat',
            name='monat',
            field=models.CharField(choices=[('Januar', 'Januar'), ('Februar', 'Februar'), ('März', 'März'), ('April', 'April'), ('Mai', 'Mai'), ('Juni', 'Juni'), ('Juli', 'Juli'), ('August', 'August'), ('September', 'September'), ('Oktober', 'Oktober'), ('November', 'November'), ('Dezember', 'Dezember')], max_length=20),
        ),
    ]
