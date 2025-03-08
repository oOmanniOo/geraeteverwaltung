from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

class Fahrzeug(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    funkrufname = models.CharField(max_length=50, unique=True, null=False)
    hersteller = models.CharField(max_length=50)
    baujahr = models.IntegerField(
        verbose_name='Baujahr',
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ]
    )
    kennzeichen = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.name} , {self.kennzeichen}"
    
class Geraeteraum(models.Model):
    fach = models.CharField(max_length=10)
    fahrzeug = models.ForeignKey(Fahrzeug, on_delete=models.CASCADE, related_name="geraeteraeume")
    
    def __str__(self):
        return f"{self.fach} vom {self.fahrzeug}"
    
