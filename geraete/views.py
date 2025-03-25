from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView

from pruefung.models import Pruefung, Naechste_Pruefung
from .models import Geraet, Kategorie
from .forms import GeraeteForm

class GeraeteListe(ListView):
    model = Geraet
    template_name = 'geraete/geraete_liste.html'
    context_object_name = 'geraete'
    paginate_by = 20

    def get_queryset(self):
        self.kategorien = Kategorie.objects.all()
        kategorie_id = self.request.GET.get('kategorie')

        if kategorie_id:
            return Geraet.objects.filter(kategorie_id=kategorie_id)
        
        return Geraet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kategorien'] = self.kategorien

        return context
        
def geraete_detail(request, id):
    geraet = get_object_or_404(Geraet, id=id)
    pruefung_status = Naechste_Pruefung.objects.filter(geraet=geraet)
    pruefungen = Pruefung.objects.filter(geraet=geraet).order_by('-datum')[:5]
    return render(request, 'geraete/geraete_detail.html', {
        'geraet': geraet,
        'pruefungen':pruefungen,
        'pruefung_status': pruefung_status
    })

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

def suche_view(request):
    query = request.GET.get("q","")
    if query:
        ergebnisse = Geraet.objects.filter(
            Q(bezeichnung__icontains=query) |
            Q(barcode__icontains=query) |
            Q(identifikation__icontains=query)
            )
        
    else:
        ergebnisse = []
    return render(request, "geraete/suche_ergebnisse.html", {"ergebnisse":ergebnisse, "query": query})