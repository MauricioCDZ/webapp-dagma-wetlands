from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('about/',views.about, name='reporte-about'),
    path('nuestraHistoria/', views.nuestraHistoria, name='reporte-nuestraHistoria'),
    path('humedales/LaBabilla/', views.LaBabilla, name='reporte-humedales-LaBabilla'),
    path('humedales/ElRetiro/', views.ElRetiro, name='reporte-humedales-ElRetiro'),
    path('humedales/EcoparqueLasGarzas/', views.EcoparqueLasGarzas, name='reporte-humedales-EcoparqueLasGarzas'),
    path('humedales/lababilla/galeria_flora', views.babilla_flora, name='reporte-humedales-flora'),
    path('humedales/lababilla/galeria_fauna', views.babilla_fauna, name='reporte-humedales-fauna'),
    path('humedales/lababilla/galeria_acuatica', views.babilla_acuatica, name='reporte-humedales-acuatica'),
    path('recursos/videos/', views.videos, name='reporte-recursos-videos'),
    path('quejas/', views.quejas, name='reporte-quejas'),
    path('registrate/', views.registrate, name='reporte-registrate'),
    path('planes_manejo/', views.planes_manejo, name='reporte-planes'),
    path('programas/', views.programas, name='reporte-programas'),
    path('hacer_reporte/', views.hacer_reporte, name='reporte-hacer-reporte'),
    path('administrador/gestionarBlog/', views.gestionarBlog, name='reporte-administrador-gestionarBlog'),
    path('administrador/gestionarReportes/', views.gestionarReportes, name='reporte-administrador-gestionarReportes'),
    path('administrador/gestionarUsuarios/', views.gestionarUsuarios, name='reporte-administrador-gestionarUsuarios'),
]