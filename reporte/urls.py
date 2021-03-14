from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reporte-home'),
    path('about/', views.about, name='reporte-about'),
]