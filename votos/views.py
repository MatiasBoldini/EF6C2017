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
    distrito = Distrito.objects.all()
    #TODO TU CODIGO AQUI
    return render(request,'global.html')

def resultado_distrital(request, id_distrito):
    distrito = Distrito.objects.get(id=id_distrito)
    cantidad = Voto.objects.filter(candididato__distrito=distrito).count()
    porcentaje_votantes = distrito.cantidad_votantes * 100 / cantidad
    total_votantes = cantidad
    #Null = True es para saber los votos validos
    voto = Voto.objects.filter(candididato__distrito=distrito, valido=True)
    ganador = Voto.objects.filter(candididato__distrito=distrito, valido=True).count()
    for a in ganador:
        if a
    ganador

    return render(request, 'distrital.html', {'distrito':distrito}, {'porcentaje_votantes': porcentaje_votantes}, {'total_votantes': total_votantes}, {'ganador': ganador})

    <li>Tamaño del padrón: {{distrito.cantidad_votantes}}</li>
    <li>Porcentaje de votantes: {{porcentaje_votantes}} </li>
    <li>Total de votos del distrito: {{total_votantes}} </li>
    <li>Candidato ganador: {{ganador}} </li>

    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}

    #TODO TU CODIGO AQUI

    return render(request,'distrital.html',context)
