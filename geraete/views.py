from django.shortcuts import render, get_object_or_404, redirect
from .models import Geraet
from pruefung.models import Pruefung
from .forms import GeraeteForm

def geraete_liste(request):
    geraete = Geraet.objects.all()
    return render(request, 'geraete/geraete_liste.html', {'geraete': geraete})

def geraete_detail(request, id):
    geraet = get_object_or_404(Geraet, id=id)
    pruefungen = Pruefung.objects.filter(geraet=geraet)
    return render(request, 'geraete/geraete_detail.html', {'geraet': geraet, 'pruefungen':pruefungen})

def geraete_create(request):
    if request.method == 'POST':
        form = GeraeteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geraete:geraete_liste')
    
    else:
        form = GeraeteForm()
        
    return render(request, 'geraete/geraete_create.html', {'form': form})

def geraete_edit(request, id):
    geraet = get_object_or_404(Geraet, id=id)

    if request.method == 'POST':
        form = GeraeteForm(request.POST, instance=geraet)

        if form.is_valid():
            identifikation = form.cleaned_data.get('identifikation')
            if Geraet.objects.exclude(id=geraet.id).filter(identifikation=identifikation).exists():
                form.add_error('identifikation', 'Dieses Gerät mit dieser Identifikation existiert bereits.')
            else:
                form.save()
                return redirect('geraete:geraete_liste')
    else:
        form = GeraeteForm(instance=geraet)

    return render(request, 'geraete/geraete_edit.html', {'form': form})