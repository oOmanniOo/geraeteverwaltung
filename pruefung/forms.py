from django import forms
from .models import Pruefung, Checkliste_Ergebnis


class PruefungForm(forms.ModelForm):
    class Meta:
        model = Pruefung
        fields = ['datum', 'pruefer', 'befund', 'art', 'bemerkung', 'geraet']

class ChecklistenErgebnisForm(forms.ModelForm):
    class Meta:
        model = Checkliste_Ergebnis
        fields = ['frage', 'antwort', 'bemerkung']
        widgets = {
            'frage': forms.HiddenInput(),
       }