from django.shortcuts import render
from .models import Geraet

def geraete_liste(request):
    geraete = Geraet.objects.all()
    return render(request, 'geraete/geraete_liste.html', {'geraete': geraete})
