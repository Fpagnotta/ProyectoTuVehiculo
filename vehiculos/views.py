from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from vehiculos.models import Autos,Motos,Camiones
from vehiculos.forms import Autos_form, Camiones_form, Motos_form

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


def cargar_autos(request):
    if request.method == "GET":
        form = Autos_form()
        context = {"form":form}
        return render (request,'cargar_vehiculos.html',context=context)
    else:
        form = Autos_form(request.POST)
        if form.is_valid():
            new_auto = Autos.objects.create(
                 marca_modelo = form.cleaned_data["marca_modelo"],
                 año = form.cleaned_data["año"],
                 transmision = form.cleaned_data["transmision"],
                 sku = form.cleaned_data["sku"],
                 precio = form.cleaned_data["precio"],
            )
            context = {"new_auto":new_auto}
        return render (request,'cargar_vehiculos.html',context=context)
 