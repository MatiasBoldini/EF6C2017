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
    distritos = Distrito.objects.all()
    candidatos = Candidato.objects.all().order_by('-cantidad_de_votos')
    padrones = Distrito.objects.all()
    votos_totales = Voto.objects.all()
    votos_candidatos = Candidato.objects.all()
    for candidato in votos_candidatos:
        candidato.cantidad_de_votos = Voto.objects.filter(candidato=candidato, valido=True).count()
        candidato.save()

    return render(request,'global.html', {'votos_nulos':votos_nulos,'votos_totales':votos_totales, 'candidato':candidatos})

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
    cantidad = Voto.objects.filter(candididato__distrito=distrito).count()
    porcentaje_votantes = distrito.cantidad_votantes * 100 / cantidad
    total_votantes = cantidad
    #Null = False es para saber los votos validos
    voto = Voto.objects.filter(candididato__distrito=distrito, valido=False)
    mayor_cantidad_de_votos = 0
    ganador = Voto.objects.filter(candididato__distrito=distrito, valido=True).count()
    return render(request, 'distrital.html', {'distrito':distrito}, {'porcentaje_votantes': porcentaje_votantes}, {'total_votantes': total_votantes}, {'ganador': ganador})

    #<li>Candidato ganador: {{ganador}} </li>
