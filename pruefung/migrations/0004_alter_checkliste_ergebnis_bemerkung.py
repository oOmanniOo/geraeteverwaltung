# Generated by Django 5.1.5 on 2025-02-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruefung', '0003_checkliste_fragen_checkliste_ergebnis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkliste_ergebnis',
            name='bemerkung',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
