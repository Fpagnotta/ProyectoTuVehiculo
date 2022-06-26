
from django.urls import path
from vehiculos.views import delete_car_view, list_car, list_motorcycle, list_truck, create_car_view, create_motorcycle_view, create_truck_view,search_vehicle, detail_car_view, detail_motorcycle_view,detail_truck_view,delete_car_view,delete_motorcycle_view,delete_truck_view, update_vehicle


urlpatterns = [
    path('cars/',list_car.as_view(),name = "cars"),
    path('motorcycles/',list_motorcycle.as_view(),name ="motorcycles"),
    path('trucks/',list_truck.as_view(),name ="trucks"),
    path('create-car/', create_car_view.as_view(),name="create_car"),
    path('create-truck/', create_truck_view.as_view(),name="create_truck"),
    path('create-motorcycle/',create_motorcycle_view.as_view(),name="create_motorcycle"),
    path('search-vehicle/',search_vehicle,name="search_vehicle"),
    path('car-details/<int:pk>/',detail_car_view.as_view(),name="car_details"),
    path('truck-details/<int:pk>/',detail_truck_view.as_view(),name="truck_details"),
    path('motorcycle-details/<int:pk>/',detail_motorcycle_view.as_view(),name="motorcycle_details"),
    path('delete-car/<int:pk>/',delete_car_view.as_view(),name="delete_car"),
    path('delete-motorcycle/<int:pk>/',delete_motorcycle_view.as_view(),name="detele_motorcycle"),
    path('delete-truck/<int:pk>/',delete_truck_view.as_view(),name="delete_truck"),
    path('update-vehicle/<int:pk>/',update_vehicle.as_view(),name="update_vehicle"),

]

