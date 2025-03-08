from django.contrib import admin
from .models import Fahrzeug, Geraeteraum

# Register your models here.
admin.site.register(Fahrzeug)
admin.site.register(Geraeteraum)