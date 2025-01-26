from django import forms
from .models import Pruefung


class PruefungForm(forms.ModelForm):
    class Meta:
        model = Pruefung
        fields = ['datum', 'pruefer', 'befund', 'art', 'bemerkung', 'geraet']
