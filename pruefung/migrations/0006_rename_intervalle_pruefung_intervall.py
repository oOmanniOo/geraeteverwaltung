# Generated by Django 5.1.5 on 2025-02-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruefung', '0005_pruefung_bestanden_pruefung_intervalle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pruefung',
            old_name='intervalle',
            new_name='intervall',
        ),
    ]
