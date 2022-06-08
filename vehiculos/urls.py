
from django.urls import path
from vehiculos.views import autos,motos,camiones,cargar_autos


urlpatterns = [
    path('autos/',autos,name = "Autos"),
    path('motos/',motos,name ="Motos"),
    path('camiones/',camiones,name ="Camiones"),
    path('cargar_autos/',cargar_autos,name="Cargar-Autos"),

]

