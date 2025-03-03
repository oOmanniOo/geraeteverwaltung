from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import modelformset_factory
from django.contrib import messages
from django.utils.timezone import now
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Pruefung, Art, Checkliste_Ergebnis, Checkliste_Fragen, Naechste_Pruefung
from .forms import PruefungForm, PruefungsFormEdit , ChecklistenErgebnisForm
from geraete.models import Geraet

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
    antworten = Checkliste_Ergebnis.objects.filter(pruefung_id = pruefung.id, )
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
    antworten = Checkliste_Ergebnis.objects.filter(pruefung_id = pruefung.id, )
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