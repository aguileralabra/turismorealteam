from django.contrib import admin
from aplicacion.models import *

class UserAdmin(admin.ModelAdmin):
    search_fields = ('cli_Rut','cli_Nombre','username')
    list_display = ('cli_Rut','cli_Nombre','username', 'is_staff','is_active','is_superuser')

admin.site.register(User, UserAdmin)
admin.site.register(Acompañante)
admin.site.register(Inventario)
admin.site.register(Gasto)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Departamento)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Conductor)
admin.site.register(Vehiculo)
admin.site.register(ServicioExtra)
admin.site.register(Transporte)
admin.site.register(Tour)
admin.site.register(Reserva)
admin.site.register(Contact)

