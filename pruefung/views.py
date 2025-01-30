from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Pruefung, Art
from geraete.models import Geraet
from .forms import PruefungForm

# Create your views here.
def pruefung_liste(request):
    pruefungen = Pruefung.objects.all()
    return render(request, 'pruefung/pruefung_liste.html', {'pruefungen' : pruefungen})

def pruefung_detail(request, id):
    pruefung = get_object_or_404(Pruefung, id=id)
    return render(request, 'pruefung/pruefung_detail.html', {'pruefung': pruefung})

def pruefung_starten(request):
    if request.method == 'POST':
        form = PruefungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pruefung:pruefungs_liste')
    
    else:
        form = PruefungForm()
    
    return render(request, 'pruefung/pruefung_durchfuehren.html', {'form': form})

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
    
    art = Art.objects.get(id=art_id)
    geraet = Geraet.objects.get(id=geraet_id)
    
    return render(request, 'pruefung/pruefung_durchfuehren.html',{
        'art': art,
        'geraet': geraet        
    })