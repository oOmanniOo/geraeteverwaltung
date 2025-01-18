from django.urls import path
from . import views

urlpatterns = [
    path('', views.geraete_liste, name='geraete_liste'),
    path('<int:id>/', views.geraete_detail, name='geraete_detail'),
]
