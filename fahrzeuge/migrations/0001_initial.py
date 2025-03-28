# Generated by Django 5.1.5 on 2025-03-04 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fahrzeug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('funkrufname', models.CharField(max_length=50, unique=True)),
                ('hersteller', models.CharField(max_length=50)),
                ('baujahr', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2025)], verbose_name='Baujahr')),
                ('kennzeichen', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
