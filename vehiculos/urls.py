
from django.urls import path
from vehiculos.views import autos, cargar_motos,motos,camiones,cargar_autos,cargar_camiones,cargar_motos,buscar_vehiculo


urlpatterns = [
    path('autos/',autos,name = "Autos"),
    path('motos/',motos,name ="Motos"),
    path('camiones/',camiones,name ="Camiones"),
    path('cargar_autos/',cargar_autos,name="Cargar-Autos"),
    path('cargar_camiones/',cargar_camiones,name="Cargar-Camiones"),
    path('cargar_motos/',cargar_motos,name="Cargar-Motos"),
    path('buscar_vehiculos/',buscar_vehiculo,name="Buscar-vehiculos"),

]

