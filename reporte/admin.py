from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Comuna)
admin.site.register(TipoHumedal)
admin.site.register(Humedales)
admin.site.register(Usuario)
admin.site.register(TipoAporte)
admin.site.register(Aporte)