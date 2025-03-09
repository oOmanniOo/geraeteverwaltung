from django.db import models
from fahrzeuge.models import Geraeteraum

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Kategorie(models.Model):
    name = models.CharField(max_length=50, unique=True, default='keine')
    
    def __str__(self):
        return self.name

class Geraet(models.Model):
    bezeichnung = models.CharField(max_length=100) 
    identifikation = models.CharField(max_length=50, unique=True)
    seriennummer = models.CharField(max_length=50, blank=True, null=True)
    hersteller = models.CharField(max_length=100, blank=True, null=True)
    kaufdatum = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)
    bemerkung = models.TextField(blank=True, null=True)
    barcode = models.PositiveIntegerField(blank=True, null=True, unique=True)
    geraeteraum = models.ForeignKey(Geraeteraum, on_delete=models.SET_NULL, null=True, unique=False, related_name='geraete')
    
    def __str__(self):
        return f"{self.bezeichnung} ({self.barcode})"
    

