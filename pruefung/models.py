from django.db import models
from geraete.models import Geraet, Kategorie
from datetime import timedelta
from dateutil.relativedelta import relativedelta

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
    bestanden = models.BooleanField()
    intervall = models.PositiveIntegerField(default=12, help_text="Intervalle in Monaten")
    
    def naechste_pruefung(self):
        if self.intervall != 0:
            return self.datum + relativedelta(months=self.intervall)
        else:
            return "keine Wiederholungsprüfung"
            
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
    bemerkung = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        constraints =[
            models.UniqueConstraint(fields=['pruefung', 'frage'], name='unique_pruefung_frage')
        ]
        
    def __str__(self):
        return f"{self.pruefung.geraet} Frage: {self.frage}"

class Naechste_Pruefung(models.Model):
    geraet = models.ForeignKey(Geraet, on_delete=models.CASCADE)
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    letzte_pruefung = models.DateField(null=True, blank=True)
    naechste_pruefung = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ('geraet', 'art')