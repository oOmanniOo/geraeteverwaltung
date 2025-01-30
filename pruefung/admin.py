from django.contrib import admin
from .models import Befund, Pruefung, Art, Checkliste_Fragen, Checkliste_Ergebnis

# Register your models here.
admin.site.register(Befund)
admin.site.register(Pruefung)
admin.site.register(Art)
admin.site.register(Checkliste_Ergebnis)
admin.site.register(Checkliste_Fragen)