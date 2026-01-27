from django.contrib import admin
from django.urls import path, include
from . import vistas


urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('inicio/', vistas.inicio,  name = 'inicio'),
    path('ranking/', vistas.ranking, name = 'ranking'),
    path('prox_partido', vistas.prox_partido, name = 'prox_partido'),
    path('partidos_terminados', vistas.partidos_terminados, name = 'partidos_terminados'),
    path('premios',vistas.premios, name = 'premios'),
]

