from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Geraet(models.Model):
    bezeichnung = models.CharField(max_length=100) 
    identifikation = models.CharField(max_length=50, unique=True)
    seriennummer = models.CharField(max_length=50, blank=True, null=True)
    hersteller = models.CharField(max_length=100, blank=True, null=True)
    kaufdatum = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.bezeichnung} ({self.identifikation})"
