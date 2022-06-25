from django.contrib import admin
from vehiculos.models import Cars,Motorcycles,Trucks

# Register your models here.
@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand','year','transmision','price','sku']
    
@admin.register(Motorcycles)
class MotorcycleAdmin(admin.ModelAdmin):
    list_display = ['brand','year','type','price','sku']    

@admin.register(Trucks)
class TruckAdmin(admin.ModelAdmin):
    list_display = ['brand','year','capacity','price','sku']
