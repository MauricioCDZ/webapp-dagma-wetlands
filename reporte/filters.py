import django_filters

from .models import Reporte

class ReporteFilter(django_filters.FilterSet):


    class Meta:
        model = Reporte
        fields = ['humedal','fecha_reporte','status','importancia']
        

class BlogFilter(django_filters.FilterSet):


    class Meta:
        model = Reporte
        fields = ['importancia']
        
