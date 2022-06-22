from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Autos(models.Model):
    marca_modelo = models.CharField (max_length=50)
    año = models.FloatField()
    transmision = models.BooleanField(blank=True)
    sku = models.CharField(max_length=30)
    precio = models.FloatField()
        
    class Meta:
        verbose_name ='Auto'
        verbose_name_plural ='Autos'
    
    
class Motos(models.Model):
    marca_modelo = models.CharField(max_length=50)
    año = models.FloatField()
    tipo = models.CharField(max_length=20)
    sku = models.CharField(max_length=30)
    precio = models.FloatField()

    class Meta:
        verbose_name ='Moto'
        verbose_name_plural ='Motos'

class Camiones(models.Model):
    marca_modelo = models.CharField (max_length=50)
    año = models.FloatField()
    capacidad = models.CharField(max_length=30)
    sku = models.CharField (max_length=30)
    precio = models.FloatField ()

    class Meta:
        verbose_name ='Camion'
        verbose_name_plural ='Camiones'