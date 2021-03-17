from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('nuestraHistoria/', views.nuestraHistoria, name='reporte-nuestraHistoria'),
    path('humedales/LaBabilla/', views.LaBabilla, name='reporte-humedales-LaBabilla'),
]