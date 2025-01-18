from django.urls import path
from . import views

urlpatterns = [
    path('', views.geraete_liste, name='geraete_liste'),
]
