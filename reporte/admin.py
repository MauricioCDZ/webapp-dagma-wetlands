from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from .models import *
class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'name','is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)
# Register your models here.
admin.site.register(Reporte)
admin.site.register(Comuna)
admin.site.register(TipoHumedal)
admin.site.register(TipoReporte)
admin.site.register(Flora)
admin.site.register(FamiliaFlora)
admin.site.register(FaunaTerrestre)
admin.site.register(FamiliaFauna)
admin.site.register(FaunaAcuatica)
admin.site.register(FloraHumedal)
admin.site.register(FaunaTerrestreHumedal)
admin.site.register(FaunaAcuaticaHumedal)
admin.site.register(InvolucrateMensaje)
admin.site.register(Humedal)
