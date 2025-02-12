from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import modelformset_factory
from .models import Pruefung, Art, Checkliste_Ergebnis, Checkliste_Fragen, Naechste_Pruefung
from geraete.models import Geraet
from .forms import PruefungForm, ChecklistenErgebnisForm
from django.contrib import messages
from django.utils.timezone import now
from .models import Naechste_Pruefung

# Create your views here.
def pruefung_liste(request):
    pruefungen = Pruefung.objects.all()
    return render(request, 'pruefung/pruefung_liste.html', {'pruefungen' : pruefungen})

def pruefung_naechste(request):
    pruefung_status = Naechste_Pruefung.objects.filter(naechste_pruefung__lt=now().date()).order_by("naechste_pruefung")
    print(pruefung_status)
    return render(request, 'pruefung/pruefung_naechste.html', {'pruefung_status': pruefung_status})

def pruefung_detail(request, id):
    pruefung = get_object_or_404(Pruefung, id=id)
    antworten = Checkliste_Ergebnis.objects.filter(pruefung_id = pruefung.id, )
    return render(request, 'pruefung/pruefung_detail.html', {'pruefung': pruefung, 'antworten' : antworten})

def pruefung_starten(request):
    if request.method == 'POST':
        form = PruefungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pruefung:pruefungs_liste')
    
    else:
        form = PruefungForm()
    
    return render(request, 'pruefung/pruefungdurchfuehrenalt.html', {'form': form})

def pruefung_auswahl(request):
    arten = Art.objects.all()
    geraete = Geraet.objects.all()

    if request.method == 'POST':
        art_id = request.POST.get('auswahlart')
        geraet_id = request.POST.get('auswahlgeraet')

        if art_id and geraet_id:
            # Richtiges Weiterleiten mit Query-Parametern
            url = reverse('pruefung:pruefung_durchfuehren') + f'?art={art_id}&geraet={geraet_id}'
            return redirect(url)
    
    return render(request, 'pruefung/pruefung_auswahl.html', {
        'arten' : arten,
        'geraete' : geraete
        })
    
def pruefung_durchfuehren(request):
    art_id = request.GET.get("art")
    geraet_id = request.GET.get("geraet")
        
    # Hole die passenden Checklisten-Fragen anhand der Prüfungsart und des Geräts
    checkliste_fragen = Checkliste_Fragen.objects.filter(art_id=art_id, kategorie__geraet=geraet_id)
    
    # Erstelle ein Formset aus der ModelForm, mit 'extra' gleich der Anzahl der gefundenen Fragen
    ChecklistenErgebnisFormSet = modelformset_factory(
        Checkliste_Ergebnis,
        form=ChecklistenErgebnisForm,
        extra=checkliste_fragen.count()
    )
    
    if request.method == "GET":
        # Für jede Frage setzen wir initial den Wert für das Feld 'frage'
        initial_data = [{'frage': frage.id} for frage in checkliste_fragen]
        formset = ChecklistenErgebnisFormSet(queryset=Checkliste_Ergebnis.objects.none(), initial=initial_data)
        zipped_forms = list(zip(formset, checkliste_fragen))
        pruefung_form = PruefungForm(art_initial=art_id, geraet_initial=geraet_id)
        context = {
            'pruefung_form': pruefung_form,
            'zipped_forms' : zipped_forms,
            'formset': formset,
            'checkliste_fragen': checkliste_fragen,
        }
        return render(request, 'pruefung/pruefung_durchfuehren.html', context)
    
    else:  # POST-Anfrage
        pruefung_form = PruefungForm(request.POST)
        formset = ChecklistenErgebnisFormSet(request.POST)

        if pruefung_form.is_valid() and formset.is_valid():
            # Speichere zuerst das Prüfungsformular, um eine Instanz zu erhalten
            pruefung_instance = pruefung_form.save()
            
            # Gehe durch jedes Formular im Formset
            for form in formset:
                if form.cleaned_data:
                    instance = form.save(commit=False)
                    # Wenn das Feld 'frage' nicht ausgefüllt wurde, setze es aus den initialen Daten
                    if not instance.frage:
                        instance.frage = form.initial.get('frage')
                    instance.pruefung = pruefung_instance
                    instance.save()
            messages.success(request, "Prüfung erfolgreich durchgeführt")
            return redirect(reverse('pruefung:pruefungs_liste'))
        else:
            context = {
                'pruefung_form': pruefung_form,
                'formset': formset,
                'checkliste_fragen': checkliste_fragen,
            }
            return render(request, 'pruefung/pruefung_durchfuehren.html', context)