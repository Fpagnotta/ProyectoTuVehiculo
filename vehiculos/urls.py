
from django.urls import path
from vehiculos.views import list_car, list_motorcycle, list_truck, create_car, create_motorcycle, create_truck,search_vehicle,autos_detalles,camiones_detalles,motos_detalles,eliminar_auto,eliminar_camion,eliminar_moto, update_vehicle


urlpatterns = [
    path('cars/',list_car,name = "Cars"),
    path('motorcycles/',list_motorcycle,name ="Motorcycles"),
    path('trucks/',list_truck,name ="Trucks"),
    path('create-car/', create_car,name="Create_Car"),
    path('create-truck/', create_truck,name="Create_Truck"),
    path('create-motorcycle/',create_motorcycle,name="Create_Motorcycle"),
    path('search-vehicle/',search_vehicle,name="Search_Vehicle"),
    path('autos_detalles/<int:pk>/',autos_detalles,name="Detalle-Autos"),
    path('camiones_detalles/<int:pk>/',camiones_detalles,name="Detalle-Autos"),
    path('motos_detalles/<int:pk>/',motos_detalles,name="Detalle-Autos"),
    path('eliminar_auto/<int:pk>/',eliminar_auto,name="Eliminar-Autos"),
    path('eliminar_moto/<int:pk>/',eliminar_moto,name="Eliminar-Motos"),
    path('eliminar_camion/<int:pk>/',eliminar_camion,name="Eliminar-Camiones"),

]

