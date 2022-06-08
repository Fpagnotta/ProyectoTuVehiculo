from django.contrib import admin
from vehiculos.models import Autos,Motos,Camiones
from vehiculos.views import autos,motos,camiones 

# Register your models here.


admin.site.register(Autos)
admin.site.register(Motos)
admin.site.register(Camiones)