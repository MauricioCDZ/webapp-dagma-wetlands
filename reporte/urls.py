from django.urls import path
from . import views
<<<<<<< HEAD
from .views import (
    ReporteListView,
    ReporteDetailView,
    ReporteCreateView,
    ReporteUpdateView,
    ReporteDeleteView,
    UserReporteListView
)


urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('nuestraHistoria/', views.nuestraHistoria, name='reporte-nuestraHistoria'),
    path('humedales/lababilla/', views.LaBabilla, name='reporte-humedales-lababilla'),
    path('humedales/lababilla/galeria_flora', views.babilla_flora, name='reporte-humedales-flora'),
    path('humedales/lababilla/galeria_fauna', views.babilla_fauna, name='reporte-humedales-fauna'),
    path('humedales/lababilla/galeria_acuatica', views.babilla_acuatica, name='reporte-humedales-acuatica'),
    path('planes_manejo/', views.planes_manejo, name='reporte-planes'),
    path('programas/', views.programas, name='reporte-programas'),
    path('hacer_reporte/', views.hacer_reporte, name='reporte-hacer-reporte'),
    path('blog/', views.blog, name='reporte-blog'),
    path('mis_reportes/', views.misreportes, name='reporte-mis-reportes'),
    path('about/', ReporteListView.as_view() , name='reporte-about'),
    path('reporte/<int:pk>/', ReporteDetailView.as_view(), name='reporte-detail'),
    path('reporte/new/', ReporteCreateView.as_view(), name='reporte-create'),
    path('reporte/<int:pk>/update/', ReporteUpdateView.as_view(), name='reporte-update'),
    path('reporte/<int:pk>/delete/', ReporteDeleteView.as_view(), name='reporte-delete'),
    path('user/<str:name>/', UserReporteListView.as_view(), name='user-reportes'),
   
]


#path('signup/', views.registro, name='reporte-signup'),
#path('signin/', views.login, name='reporte-signin'),
#path('login/', views.login1, name='reporte-login'),
=======

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
>>>>>>> 5752ea43f40a6c0470a69916c429a8a7c275278e
