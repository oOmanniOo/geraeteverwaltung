from django.db import models
from geraete.models import Geraet, Kategorie

# Create your models here.
class Befund(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Art(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Pruefung(models.Model):
    datum = models.DateField(blank=False, null=True)
    pruefer = models.CharField(max_length=50, null=False, blank=True)
    befund = models.ForeignKey(Befund, on_delete=models.PROTECT, null=False)
    art = models.ForeignKey(Art, on_delete=models.PROTECT, null=False)
    bemerkung = models.TextField(null=True, blank=True)
    geraet = models.ForeignKey(Geraet, on_delete=models.PROTECT, null=False)
    
    def __str__(self):
        return f"{self.geraet} wurde am {self.datum} geprüft"
    
class Checkliste_Fragen(models.Model):
    art = models.ForeignKey(Art, on_delete=models.PROTECT)
    kategorie = models.ForeignKey(Kategorie, on_delete=models.PROTECT)
    frage = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.frage
    
class Checkliste_Ergebnis(models.Model):
    pruefung = models.ForeignKey(Pruefung, on_delete=models.PROTECT, null=False)
    frage = models.ForeignKey(Checkliste_Fragen, on_delete=models.PROTECT, null=False)
    antwort = models.BooleanField()
    bemerkung = models.TextField(blank=True, null=True)
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['pruefung', 'frage'], name='unique_pruefung_frage')
        ]