from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('about/',views.about, name='reporte-about'),
    path('nuestraHistoria/', views.nuestraHistoria, name='reporte-nuestraHistoria'),
    path('humedales/lababilla/', views.LaBabilla, name='reporte-humedales-LaBabilla'),
    path('humedales/lababilla/galeria_flora', views.babilla_flora, name='reporte-humedales-flora'),
    path('humedales/lababilla/galeria_fauna', views.babilla_fauna, name='reporte-humedales-fauna'),
    path('humedales/lababilla/galeria_acuatica', views.babilla_acuatica, name='reporte-humedales-acuatica'),
    path('planes_manejo/', views.planes_manejo, name='reporte-planes'),
    path('programas/', views.programas, name='reporte-programas'),
    path('hacer_reporte/', views.hacer_reporte, name='reporte-hacer-reporte')
]