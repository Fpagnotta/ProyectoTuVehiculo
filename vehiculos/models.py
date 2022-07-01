from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Cars(models.Model):
    brand = models.CharField (max_length=50)
    year = models.FloatField()
    transmision = models.BooleanField(blank=True)
    sku = models.CharField(max_length=30)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
        
    class Meta:
        verbose_name ='car'
        verbose_name_plural ='cars'

    def __str__(self):
        return self.brand

class Motorcycles(models.Model):
    brand = models.CharField(max_length=50)
    year = models.FloatField()
    type = models.CharField(max_length=20)
    sku = models.CharField(max_length=30)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name ='motorcyle'
        verbose_name_plural ='motorcycles'

    def __str__(self):
        return self.brand

class Trucks(models.Model):
    brand = models.CharField (max_length=50)
    year = models.FloatField()
    capacity = models.CharField(max_length=30)
    sku = models.CharField (max_length=30)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name ='truck'
        verbose_name_plural ='trucks'
    
    def __str__(self):
        return self.brand