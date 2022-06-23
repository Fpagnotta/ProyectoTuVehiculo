
from django.urls import path
from vehiculos.views import autos, cargar_motos,motos,camiones,cargar_autos,cargar_camiones,cargar_motos,buscar_vehiculo,autos_detalles,camiones_detalles,motos_detalles,eliminar_auto,eliminar_camion,eliminar_moto


urlpatterns = [
    path('autos/',autos,name = "Autos"),
    path('motos/',motos,name ="Motos"),
    path('camiones/',camiones,name ="Camiones"),
    path('cargar_autos/',cargar_autos,name="Cargar-Autos"),
    path('cargar_camiones/',cargar_camiones,name="Cargar-Camiones"),
    path('cargar_motos/',cargar_motos,name="Cargar-Motos"),
    path('buscar_vehiculos/',buscar_vehiculo,name="Buscar-vehiculos"),
    path('autos_detalles/<int:pk>/',autos_detalles,name="Detalle-Autos"),
    path('camiones_detalles/<int:pk>/',camiones_detalles,name="Detalle-Autos"),
    path('motos_detalles/<int:pk>/',motos_detalles,name="Detalle-Autos"),
    path('eliminar_auto/<int:pk>/',eliminar_auto,name="Eliminar-Autos"),
    path('eliminar_moto/<int:pk>/',eliminar_moto,name="Eliminar-Motos"),
    path('eliminar_camion/<int:pk>/',eliminar_camion,name="Eliminar-Camiones"),

]

