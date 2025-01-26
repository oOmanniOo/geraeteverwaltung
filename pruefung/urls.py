from django.urls import path
from . import views
 
app_name = 'pruefung'

urlpatterns = [
    path('', views.pruefung_liste, name='pruefungs_liste'),
    path('<int:id>/', views.pruefung_detail, name='pruefung_detail'),
    path('pruefen/', views.pruefung_starten, name='pruefung_durchfueren'),
]

