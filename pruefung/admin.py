from django.contrib import admin
from .models import Befund, Pruefung, Art, Checkliste_Fragen, Checkliste_Ergebnis, Naechste_Pruefung, Fahrzeug_Pruefung, Fahrzeug_Checkliste_Ergebnis, Fahrzeug_Fragen, Fahrzeug_Vorlage, Monat

# Register your models here.
admin.site.register(Befund)
admin.site.register(Pruefung)
admin.site.register(Art)
admin.site.register(Checkliste_Ergebnis)
admin.site.register(Checkliste_Fragen)
admin.site.register(Naechste_Pruefung)
admin.site.register(Fahrzeug_Fragen)
admin.site.register(Fahrzeug_Vorlage)
admin.site.register(Fahrzeug_Pruefung)
admin.site.register(Fahrzeug_Checkliste_Ergebnis)
admin.site.register(Monat)