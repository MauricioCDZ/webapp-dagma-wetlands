from django.apps import AppConfig
from django.conf import settings
import os



class ReporteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reporte'
    #path = os.path.join(settings.BASE_DIR, 'reporte')