# Generated by Django 5.1.5 on 2025-01-21 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geraete', '0004_rename_katgorie_geraet_kategorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Befund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pruefung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('datum', models.DateField(null=True)),
                ('pruefer', models.CharField(blank=True, max_length=50)),
                ('bemerkung', models.TextField(blank=True, null=True)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruefung.art')),
                ('befund', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pruefung.befund')),
                ('geraet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='geraete.geraet')),
            ],
        ),
    ]
