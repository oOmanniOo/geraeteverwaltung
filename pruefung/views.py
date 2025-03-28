from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib import messages
from django.utils.timezone import now
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db import transaction

from .models import Pruefung, Art, Checkliste_Ergebnis, Checkliste_Fragen, Naechste_Pruefung, Fahrzeug_Pruefung, Fahrzeug_Checkliste_Ergebnis, Fahrzeug_Vorlage, Monat
from .forms import PruefungForm, PruefungsFormEdit , ChecklistenErgebnisForm, FahrzeugChecklistenErgebnisForm, FahrzeugPruefFormCreate
from geraete.models import Geraet
from fahrzeuge.models import Fahrzeug

from weasyprint import HTML

# Create your views here.
def pruefung_liste(request):
    pruefungen = Pruefung.objects.all()
    paginator = Paginator(pruefungen,25)
    
    page_number = request.GET.get("Seite")
    page_obj = paginator.get_page(page_number) 
    return render(request, 'pruefung/pruefung_liste.html', {'page_obj' : page_obj})

def pruefung_naechste(request):
    pruefung_status = Naechste_Pruefung.objects.filter(naechste_pruefung__lt=now().date()).order_by("naechste_pruefung")
    print(pruefung_status)
    return render(request, 'pruefung/pruefung_naechste.html', {'pruefung_status': pruefung_status})

def pruefung_detail(request, id):
    pruefung = get_object_or_404(Pruefung, id=id)
    antworten = Checkliste_Ergebnis.objects.filter(pruefung_id = pruefung.id )
    return render(request, 'pruefung/pruefung_detail.html', {'pruefung': pruefung, 'antworten' : antworten})

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
        
def generate_pdf(request, id):
    pruefung = get_object_or_404(Pruefung, id=id)
    antworten = Checkliste_Ergebnis.objects.filter(pruefung_id = pruefung.id )
    html_string = render_to_string('pruefung/pdf_template.html', {'pruefung': pruefung, 'antworten' : antworten})
    
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="pruefung.pdf"'
    return response

def pruefung_edit(request, id):
    pruefung = get_object_or_404(Pruefung, id=id)
    ChecklistenErgebnisFormset = modelformset_factory(Checkliste_Ergebnis, form=ChecklistenErgebnisForm, extra=0)
    print(request.POST) 
    if request.method == "POST":
        pruefung_form = PruefungsFormEdit(request.POST, instance=pruefung)
        antwort_formset = ChecklistenErgebnisFormset(request.POST, queryset=Checkliste_Ergebnis.objects.filter(pruefung=pruefung))

        if pruefung_form.is_valid() and antwort_formset.is_valid():
            pruefung_form.save()
            antwort_formset.save()
            return redirect(reverse('pruefung:pruefung_detail', kwargs={'id': pruefung.id}))

    else:
        pruefung_form = PruefungsFormEdit(instance=pruefung)
        antwort_formset = ChecklistenErgebnisFormset(queryset=Checkliste_Ergebnis.objects.filter(pruefung=pruefung))

    return render(request, 'pruefung/pruefung_edit.html', {
        'pruefung_form': pruefung_form,
        'antwort_formset': antwort_formset,
        'pruefung': pruefung
    })
    
def fahrzeug_pruefung_liste(request):
    pruefungen = Fahrzeug_Pruefung.objects.all()
    paginator = Paginator(pruefungen,25)
    
    page_number = request.GET.get("Seite")
    page_obj = paginator.get_page(page_number) 
    return render(request, 'pruefung/fahrzeug_pruefung_liste.html', {'page_obj' : page_obj})

def fahrzeug_pruefung_detail(request, id):
    pruefung = get_object_or_404(Fahrzeug_Pruefung, id=id)
    checkliste =Fahrzeug_Checkliste_Ergebnis.objects.filter(pruefung = pruefung)
    
    return render(request, 'pruefung/fahrzeug_pruefung_detail.html', {
        'pruefung': pruefung,
        'checkliste':checkliste
    })
    
def fahrzeug_pruefung_durchfuehren(request):
    fahrzeug_id = request.GET.get('fahrzeug')
    monat_id = request.GET.get('monat')
    
    fahrzeug = get_object_or_404(Fahrzeug, id=fahrzeug_id)
    monat = get_object_or_404(Monat, id=monat_id)
    
    
    checklisten_fragen = Fahrzeug_Vorlage.objects.filter(fahrzeug=fahrzeug, monat=monat)
    
    ChecklisteFahrzeugErgebnisFormSet = modelformset_factory(
        Fahrzeug_Checkliste_Ergebnis,
        form = FahrzeugChecklistenErgebnisForm,
        extra = checklisten_fragen.count()
    )
    
    if request.method == "GET":
        initial_data = [{'frage': frage} for frage in checklisten_fragen]
        formset = ChecklisteFahrzeugErgebnisFormSet(
            queryset = Fahrzeug_Checkliste_Ergebnis.objects.none(),
            initial=initial_data
        )
        zipped_forms = list(zip(formset, checklisten_fragen))
        
        pruefung_form = FahrzeugPruefFormCreate(initial={'fahrzeug': fahrzeug, 'monat': monat})
        print(fahrzeug)
        context = {
            'pruefung_form':pruefung_form,
            'formset':formset,
            'zipped_forms':zipped_forms,
            'checklisten_fragen':checklisten_fragen,
            'fahrzeug':fahrzeug,
            'monat':monat,
        }
        
        return render(request,'pruefung/fahrzeug_pruefung_durchfuehren.html', context) 

    else:
        pruefung_form = FahrzeugPruefFormCreate(request.POST)
        formset = ChecklisteFahrzeugErgebnisFormSet(request.POST)
        
        if pruefung_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                # Speichere zuerst das Prüfungsformular, um die Instanz zu erhalten
                pruefung_instance = pruefung_form.save(commit=False)
                pruefung_instance.fahrzeug = fahrzeug  # Sicherstellen, dass das Fahrzeug gesetzt wird
                pruefung_instance.monat = monat        # und der Monat
                pruefung_instance.save()
                
                # Iteriere über das Formset und speichere die Checklisten-Ergebnisse
                for form in formset:
                    if form.cleaned_data:
                        instance = form.save(commit=False)
                        # Falls das Feld 'frage' nicht befüllt wurde, setze es aus den initialen Daten
                        if not instance.frage:
                            instance.frage = form.initial.get('frage')
                        instance.pruefung = pruefung_instance
                        instance.save()
            
            messages.success(request, "Prüfung erfolgreich durchgeführt")
            return redirect(reverse('fahrzeuge:fahrzeug_detail' , kwargs={'id': fahrzeug.id} ))
        else:
            messages.error(request, "Es gab ein Problem mit der Eingabe. Bitte überprüfe die Formulare.")
            context = {
                'pruefung_form': pruefung_form,
                'formset': formset,
                'zipped_forms': list(zip(formset, checklisten_fragen)),
                'checklisten_fragen': checklisten_fragen,
                'fahrzeug': fahrzeug,
                'monat': monat,
            }
            return render(request, 'pruefung/fahrzeug_pruefung_durchfuehren.html', context)        
