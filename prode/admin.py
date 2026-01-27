from django.contrib import admin
from .models import Equipo, Partido

admin.site.register(Equipo)

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('equipo_local', 'equipo_visitante', 'fecha', 'hora_24', 'jugado')  # Usa 'hora_24' en lugar de 'hora'
    list_display_links = ('fecha',)

    def hora_24(self, obj):
        return obj.hora.strftime('%H:%M')  # Formato 24 horas
    hora_24.short_description = 'Hora'  # Nombre de la columna