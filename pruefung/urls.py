from django.urls import path
from . import views
 
app_name = 'pruefung'

urlpatterns = [
    path('', views.pruefung_liste, name='pruefungs_liste'),
    path('naechste/', views.pruefung_naechste, name='pruefung_naechste'),
    path('<int:id>/', views.pruefung_detail, name='pruefung_detail'),
    path('<int:id>/edit/', views.pruefung_edit, name='pruefung_edit'),
    path('auswahl/', views.pruefung_auswahl, name='pruefung_auswahl'),
    path('durchfuehren/', views.pruefung_durchfuehren, name='pruefung_durchfuehren'),
    path('fahrzeuge/', views.fahrzeug_pruefung_liste, name='fahrzeug_pruefungs_liste'),
    path('fahrzeuge/durchfuehren/', views.fahrzeug_pruefung_durchfuehren, name='fahrzeug_pruefungs_durchfuehren'),
    path('fahrzeuge/<int:id>/', views.fahrzeug_pruefung_detail, name='fahrzeug_pruefungs_detail'),
    path('pdf/<int:id>/', views.generate_pdf, name='pdf_erzeugen'),
]

