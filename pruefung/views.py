from django.shortcuts import render
from .models import Pruefung

# Create your views here.
def pruefung_liste(request):
    pruefungen = Pruefung.objects.all()
    return render(request, 'pruefung/pruefung_liste.html', {'pruefungen' : pruefungen})