from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Longitud', max_digits=14, decimal_places=10, default=0)

    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    Se decide utilizar este modelo para la clase candidato porque es
    necesario saber a que Distrito pertenece, y se le agrega un nombre
    por temas esteticos.
    """
    nombre = models.CharField('Nombre del candidato', max_length=25)
    distrito = models.ForeignKey(Distrito)
    cantidad_de_votos = models.IntegerField('Cantidad de votos', default=0)
    porcentaje = models.IntegerField('Porcentaje de votos', default=0)

    def __str__(self):
        return 'Candidato {} tuvo {} voto'.format(self.nombre, self.cantidad_de_votos)

class Voto(models.Model):
    """
    Se decide utilizar este modelo para la clase votos porque es
    necesario saber a que Candidato pertenece, y un boolean (valido)
    para saber como debe ser contado el mismo, como valido o nulo
    """
    candidato = models.ForeignKey(Candidato)
    valido = models.BooleanField(null=False)
