from django.contrib import admin
from vehiculos.models import Autos,Motos,Camiones
from vehiculos.views import autos,motos,camiones 

# Register your models here.



@admin.register(Autos)
class AutosAdmin(admin.ModelAdmin):
    list_display = ['marca_modelo','año','transmision','precio','sku']
    
@admin.register(Motos)
class MotosAdmin(admin.ModelAdmin):
    list_display = ['marca_modelo','año','tipo','precio','sku']    

@admin.register(Camiones)
class CamionesAdmin(admin.ModelAdmin):
    list_display = ['marca_modelo','año','capacidad','precio','sku']
