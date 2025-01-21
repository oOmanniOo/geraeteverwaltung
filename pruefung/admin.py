from django.contrib import admin
from .models import Befund, Pruefung, Art

# Register your models here.
admin.site.register(Befund)
admin.site.register(Pruefung)
admin.site.register(Art)