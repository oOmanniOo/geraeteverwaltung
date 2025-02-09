from django import forms
from .models import Pruefung, Checkliste_Ergebnis, Art
from geraete.models import Geraet


class PruefungForm(forms.ModelForm):
    art_display = forms.CharField(label="Prüfungsart", required=False, disabled=True)
    geraet_display = forms.CharField(label="Gerät", required=False, disabled=True)
    
    class Meta:
        model = Pruefung
        fields = ['datum','art_display', 'geraet_display', 'pruefer', 'befund', 'art','bemerkung', 'geraet', 'bestanden', 'intervall']
        widgets = {
            'datum': forms.DateInput(attrs={'type': 'date'}),
            'art': forms.HiddenInput(),
            'geraet': forms.HiddenInput(),
        }
        
        
    def __init__(self, *args, **kwargs):
        art_initial = kwargs.pop('art_initial', None)
        geraet_initial = kwargs.pop('geraet_initial', None)
        super().__init__(*args, **kwargs)
        
        if art_initial:
            self.fields['art'].initial = art_initial
            try:
                art_obj = Art.objects.get(id=art_initial)
                self.fields['art_display'].initial = str(art_obj)
            except Art.DoesNotExist:
                self.fields['art_display'].initial = ""
        
        if geraet_initial:
            self.fields['geraet'].initial = art_initial
            try:
                geraet_obj = Geraet.objects.get(id=geraet_initial)
                self.fields['geraet_display'].initial = str(geraet_obj)
            except Geraet.DoesNotExist:
                self.fields['geraet_display'].initial = ""


class ChecklistenErgebnisForm(forms.ModelForm):
    class Meta:
        model = Checkliste_Ergebnis
        fields = ['frage', 'antwort', 'bemerkung']
        widgets = {
            'frage': forms.HiddenInput(),
       }