from django.db.models.signals import post_save
from django.db.models import Max
from django.dispatch import receiver
from .models import Pruefung, Naechste_Pruefung	
from dateutil.relativedelta import relativedelta

@receiver(post_save, sender=Pruefung)
def update_nachstepruefung(sender, instance, **kwargs):
    geraet = instance.geraet
    art = instance.art
    
    status, created = Naechste_Pruefung.objects.get_or_create(geraet=geraet, art=art)

    neuestes_datum = Pruefung.objects.filter(geraet=geraet, art=art).aggregate(Max("datum"))["datum__max"]
    print(instance.intervall)
    
    if neuestes_datum:
        status.letzte_pruefung = neuestes_datum
    print(instance.datum)
    status.naechste_pruefung = instance.datum + relativedelta(months=instance.intervall)
    print(f"Naechste Prüfung: {status.naechste_pruefung}")
    print(f"letzte Prüfung: {neuestes_datum}")
    

    
    status.save()