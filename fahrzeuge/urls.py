from django.urls import path
from . import views

app_name = 'fahrzeuge'

urlpatterns = [
    path('', views.fahrzeuge_liste, name='fahrzeuge_liste'),
    path('<int:id>/', views.fahrzeug_detail, name='fahrzeug_detail'),
]
