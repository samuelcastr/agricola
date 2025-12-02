from django.db import models

from cultivos.models import Cultivo


"""class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
"""

class Cosecha(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_cosecha = models.DateField()
    cantidad = models.FloatField()
    descripcion = models.TextField(blank=True)
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre

