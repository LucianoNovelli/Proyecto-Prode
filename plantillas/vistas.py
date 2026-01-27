from django.shortcuts import render
from prode.models import Equipo
# Create your views here.

def inicio(request):
    equipos = Equipo.objects.all()
    return render(request,'inicio.html', {"equipos": equipos})

def ranking(request):
    return render (request,'ranking.html',{})

def prox_partido(request):
    return render (request, 'prox_partido.html')

def partidos_terminados (request):
    return render (request, 'partidos_terminados.html')

def premios (request):
    return render (request, 'premios.html')
