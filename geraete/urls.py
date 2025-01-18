from django.urls import path
from . import views
 
app_name = 'geraete' 

urlpatterns = [
    path('', views.geraete_liste, name='geraete_liste'),
    path('<int:id>/', views.geraete_detail, name='geraete_detail'),
    path('create/', views.geraete_create, name='geraete_create'),
    path('<int:id>/edit/', views.geraete_edit, name='geraete_edit'),
]
