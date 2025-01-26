from django.shortcuts import render, get_object_or_404, redirect
from .models import Pruefung
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