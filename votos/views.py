# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    votos_nulos = Voto.objects.filter(valido=False)
    distrito = Distrito.objects.all()
    candidatos = Candidato.objects.all().order_by('-cantidad_de_votos')
    votos_totales = Voto.objects.all()
    votos_candidatos = Candidato.objects.all()

    for candidato in votos_candidatos:
        candidato.cantidad_de_votos = Voto.objects.filter(candidato=candidato, valido=True).count()
        candidato.cantidad_de_nulos = Voto.objects.filter(candidato=candidato, valido=False).count()
        candidato.porcentaje = Voto.objects.filter(candidato=candidato, valido=True).count()*100 / Voto.objects.filter(candidato__distrito=distrito).count()
        candidato.porcentaje_nulos = Voto.objects.filter(candidato=candidato, valido=False).count()*100 / Voto.objects.filter(candidato__distrito=distrito, valido=False).count()
        candidato.save()

    return render(request,'global.html', {'votos_nulos':votos_nulos,'votos_totales':votos_totales, 'candidato':candidatos, 'todos_los_distritos':distrito})

def distrital(request, id_distrito):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    distrito = Distrito.objects.get(id=id_distrito)
    total_votantes = Voto.objects.filter(candidato__distrito=distrito).count()
    padron = distrito.cantidad_votantes
    #Null = False es para saber los votos validos
    porcentaje_votantes = Voto.objects.filter(candidato__distrito=distrito).count()*100/padron
    return render(request, 'distrital.html', {'distrito':distrito, 'total_votantes': total_votantes, 'porcentaje_votantes':porcentaje_votantes})
