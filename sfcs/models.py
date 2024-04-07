from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.

class Almacen(models.Model):
    creado_en = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=100)
    medida = models.CharField(max_length=100)
    clase = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150)
    valor = models.FloatField(max_length=15)
    lista_medidas = models.CharField(max_length=100)

    objects = DataFrameManager()

    def __str__(self):
        return(f'{self.creado_en} {self.descripcion}')