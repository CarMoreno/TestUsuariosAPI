from django.db import models

"""Modelo Usuarios"""

class Usuario(models.Model):
    nombre = models.CharField(max_length=120, blank=False)
    apellido = models.CharField(max_length=120, blank=False)
    direccion = models.CharField(max_length=180, blank=False)
    ciudad = models.CharField(max_length=120, blank=False)
    longitud = models.FloatField(null=True, default=None)
    latitud = models.FloatField(null=True, default=None)
    estadogeo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre