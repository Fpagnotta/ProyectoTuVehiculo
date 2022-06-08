from multiprocessing import context
from django.shortcuts import render
from vehiculos.models import Autos,Motos,Camiones

# Create your views here.


def autos(request):
    autos = Autos.objects.all()
    context={'autos':autos}
    return render(request,'autos.html',context=context)




def motos(request):
    motos = Motos.objects.all()                          
    context={'motos':motos}
    return render(request,'motos.html',context=context)




def camiones(request):
    camiones = Camiones.objects.all()        
    context={'camiones':camiones}
    return render(request,'camionetas.html',context=context)

def cargar_vehiculos(request):
    context ={'cargar_vehiculo':cargar_vehiculos}
    return render (request,'cargar_vehiculos.html',context)
 