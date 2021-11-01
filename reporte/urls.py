from django.urls import path
from . import views
from .views import (
    ReporteListView,
    ReporteDetailView,
    ReporteCreateView,
    ReporteStatusView,
    ReporteUpdateView,
    ReporteDeleteView,
    UserReporteListView,
    gestionarReportes,
    ReporteCreateViewInvitado
)


urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('nuestra_historia/', views.nuestraHistoria, name='reporte-nuestraHistoria'),
    path('humedales/la_babilla/', views.LaBabilla, name='reporte-humedales-lababilla'),
    path('humedales/el_retiro/', views.ElRetiro, name='reporte-humedales-ElRetiro'),
    path('humedales/ecoparque_las_garzas/', views.EcoparqueLasGarzas, name='reporte-humedales-EcoparqueLasGarzas'),
    path('humedales/la_babilla/galeria_flora', views.babilla_flora, name='reporte-babilla-flora'),
    path('humedales/la_babilla/galeria_fauna_terrestre', views.babilla_fauna, name='reporte-babilla-fauna'),
    path('humedales/la_babilla/galeria_fauna_acuatica', views.babilla_acuatica, name='reporte-babilla-acuatica'),
    path('humedales/las_garzas/galeria_flora', views.garzas_flora, name='reporte-garzas-flora'),
    path('humedales/las_garzas/galeria_fauna_terrestre', views.garzas_fauna, name='reporte-garzas-fauna'),
    path('humedales/las_garzas/galeria_fauna_acuatica', views.garzas_acuatica, name='reporte-garzas-acuatica'),
    path('humedales/el_retiro/galeria_flora', views.retiro_flora, name='reporte-retiro-flora'),
    path('humedales/el_retiro/galeria_fauna_terrestre', views.retiro_fauna, name='reporte-retiro-fauna'),
    path('humedales/el_retiro/galeria_fauna_acuatica', views.retiro_acuatica, name='reporte-retiro-acuatica'),
    path('recursos/planes_manejo/', views.planes_manejo, name='reporte-planes'),
    path('recursos/programas/', views.programas, name='reporte-programas'),
    path('recursos/videos/', views.videos, name='reporte-recursos-videos'),
    path('hacer_reporte/', ReporteCreateViewInvitado.as_view() , name='reporte-hacer-reporte'),
    path('involucrate/', views.involucrate, name='reporte-involucrate'),
    path('blog/', views.blog, name='reporte-blog'),
    path('mis_reportes/', views.misreportes, name='reporte-mis-reportes'),
    path('about/', ReporteListView.as_view() , name='reporte-about'),
    path('quejas/', views.quejas, name='reporte-quejas'),
    path('administrador/gestionar_blog/', views.gestionarBlog, name='reporte-administrador-gestionarBlog'),
    path('administrador/gestionar_reportes/', views.gestionarReportes, name='reporte-administrador-gestionarReportes'),
    path('administrador/gestionar_usuarios/', views.gestionarUsuarios, name='reporte-administrador-gestionarUsuarios'),
    path('reporte/<int:pk>/', ReporteDetailView.as_view(), name='reporte-detail'),
    path('reporte/new/', ReporteCreateView.as_view(), name='reporte-create'),
    path('reporte/<int:pk>/update/', ReporteUpdateView.as_view(), name='reporte-update'),
    path('reporte/<int:pk>/delete/', ReporteDeleteView.as_view(), name='reporte-delete'),
    path('reporte/<int:pk>/update1/', ReporteStatusView.as_view(template_name='reporte/reporte_update1.html'), name='reporte-update1'),
    path('user/<str:name>/', UserReporteListView.as_view(), name='user-reportes'),
    path('login1/', views.login1, name='reporte-login1'),
   
]


#path('signup/', views.registro, name='reporte-signup'),
#path('signin/', views.login, name='reporte-signin'),
#path('login/', views.login1, name='reporte-login'),