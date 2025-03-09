from django import forms
from .models import Geraet

class GeraeteForm(forms.ModelForm):
    class Meta:
        model = Geraet
        fields = [
            'seriennummer',
            'identifikation',
            'status',
            'hersteller',
            'kaufdatum',
            'bemerkung',
            'kategorie',
            'barcode',
            'geraeteraum',
            'inventarnummer',
        ]