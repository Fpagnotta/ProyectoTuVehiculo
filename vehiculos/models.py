from pyexpat import model
from django.db import models

# Create your models here.

class Autos(models.Model):
    marca_modelo = models.CharField (max_length=50)
    año = models.FloatField()
    transmision = models.BooleanField(blank=True)
    sku = models.CharField(max_length=30)
    precio = models.FloatField()
    
    
class Motos(models.Model):
    marca_modelo = models.CharField(max_length=50)
    año = models.FloatField()
    tipo = models.CharField(max_length=20)
    sku = models.CharField(max_length=30)
    precio = models.FloatField()

class Camiones(models.Model):
    marca_modelo = models.CharField (max_length=50)
    año = models.FloatField()
    capacidad = models.CharField(max_length=30)
    sku = models.CharField (max_length=30)
    precio = models.FloatField ()