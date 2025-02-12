from django.urls import path
from . import views
 
app_name = 'pruefung'

urlpatterns = [
    path('', views.pruefung_liste, name='pruefungs_liste'),
    path('naechste/', views.pruefung_naechste, name='pruefung_naechste'),
    path('<int:id>/', views.pruefung_detail, name='pruefung_detail'),
    path('pruefen/', views.pruefung_starten, name='pruefung_starten'),
    path('auswahl/', views.pruefung_auswahl, name='pruefung_auswahl'),
    path('durchfuehren/', views.pruefung_durchfuehren, name='pruefung_durchfuehren'),
]

