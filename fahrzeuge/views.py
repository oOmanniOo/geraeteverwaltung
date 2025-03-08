from django.shortcuts import render, get_object_or_404

from .models import Fahrzeug, Geraeteraum
from geraete.models import Geraet

def fahrzeuge_liste(request):
    fahrzeuge = Fahrzeug.objects.all()

    return render(request, 'fahrzeuge/fahrzeuge_liste.html',{'fahrzeuge':fahrzeuge})

def fahrzeug_detail(request, id):
    fahrzeug = get_object_or_404(Fahrzeug, id=id)
    geraeteraeume = Geraeteraum.objects.filter(fahrzeug=fahrzeug)
    geraete = Geraet.objects.filter(geraeteraum__in=geraeteraeume)
    print(geraeteraeume)

     
    return render(request, 'fahrzeuge/fahrzeug_detail.html', {
        'fahrzeug':fahrzeug,
        'geraeteraume':geraeteraeume,
        "geraete": geraete,
        })

