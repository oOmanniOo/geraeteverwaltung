from django.shortcuts import render, get_object_or_404
from .models import Geraet

def geraete_liste(request):
    geraete = Geraet.objects.all()
    return render(request, 'geraete/geraete_liste.html', {'geraete': geraete})

def geraete_detail(request, id):
    geraet = get_object_or_404(Geraet, id=id)
    return render(request, 'geraete/geraete_detail.html', {'geraet': geraet})