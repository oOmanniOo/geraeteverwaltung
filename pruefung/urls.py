from django.urls import path
from . import views
 
app_name = 'pruefung'

urlpatterns = [
    path('', views.pruefung_liste, name='pruefungs_liste')    
]

