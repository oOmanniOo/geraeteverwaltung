from django.urls import path
from . import views
 
app_name = 'geraete' 

urlpatterns = [
    path('<int:id>/', views.geraete_detail, name='geraete_detail'),
    path('create/', views.geraete_create, name='geraete_create'),
    path('<int:id>/edit/', views.geraete_edit, name='geraete_edit'),
    path('suche/', views.suche_view, name='suche'),
    path('', views.GeraeteListe.as_view(), name='geraete_liste')
]
