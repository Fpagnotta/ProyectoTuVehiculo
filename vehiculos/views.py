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
        return render (request,'cargar_autos.html',context=context)
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
        return render (request,'cargar_autos.html',context=context)

def cargar_camiones(request):
    if request.method == "GET":
        form = Camiones_form()
        context = {"form":form}
        return render (request,'cargar_camiones.html',context=context)
    else:
        form = Camiones_form(request.POST)
        if form.is_valid():
            new_camion = Camiones.objects.create(
                 marca_modelo = form.cleaned_data["marca_modelo"],
                 año = form.cleaned_data["año"],
                 transmision = form.cleaned_data["transmision"],
                 sku = form.cleaned_data["sku"],
                 precio = form.cleaned_data["precio"],
            )
            context = {"new_camion":new_camion}
        return render (request,'cargar_camiones.html',context=context)
 
def cargar_motos(request):
    if request.method == "GET":
        form = Motos_form()
        context = {"form":form}
        return render (request,'cargar_motos.html',context=context)
    else:
        form = Motos_form(request.POST)
        if form.is_valid():
            new_moto = Motos.objects.create(
                 marca_modelo = form.cleaned_data["marca_modelo"],
                 año = form.cleaned_data["año"],
                 transmision = form.cleaned_data["transmision"],
                 sku = form.cleaned_data["sku"],
                 precio = form.cleaned_data["precio"],
            )
            context = {"new_moto":new_moto}
        return render (request,'cargar_motos.html',context=context)

def buscar_vehiculo(request):
    print(request.GET)
    autos = Autos.objects.filter(marca_modelo = request.GET["Search"])
    camiones = Camiones.objects.filter(marca_modelo = request.GET["Search"])
    motos = Motos.objects.filter(marca_modelo = request.GET["Search"])
    context = {"autos":autos, "camiones": camiones, "motos":motos}
    return render(request,"buscar_vehiculo.html", context = context)