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
    return render(request,'camiones.html',context=context)








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
                 capacidad = form.cleaned_data["capacidad"],
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
                 tipo = form.cleaned_data["tipo"],
                 sku = form.cleaned_data["sku"],
                 precio = form.cleaned_data["precio"],
            )
            context = {"new_moto":new_moto}
        return render (request,'cargar_motos.html',context=context)








def buscar_vehiculo(request):
    print(request.GET)
    camiones = Camiones.objects.filter(marca_modelo__contains = request.GET["Search"])
    autos = Autos.objects.filter(marca_modelo__contains = request.GET["Search"])
    motos = Motos.objects.filter(marca_modelo__contains = request.GET["Search"])
    context = {"autos":autos, "camiones": camiones, "motos":motos}
    return render(request,"buscar_vehiculo.html", context = context)










def autos_detalles(request, pk):
    try:
        autos = Autos.objects.get(id=pk)
        context = {'auto':autos}
        return render(request,'autos_detalles.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'autos.html',context=context)    


def motos_detalles(request, pk):
    try:
        motos = Motos.objects.get(id=pk)
        context = {'moto':motos}
        return render(request,'motos_detalles.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'motos.html',context=context)    

def camiones_detalles(request, pk):
    try:
        camiones = Camiones.objects.get(id=pk)
        context = {'camion':camiones}
        return render(request,'camiones_detalles.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'camiones.html',context=context)    





def eliminar_auto (request,pk):
    try:
        auto= Autos.objects.get (id=pk)
        auto.delete()
        context = {'mensaje':"El auto se ha eliminado correctamente"}
        return render(request,'autos.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'autos.html',context=context)  


def eliminar_moto (request,pk):
    try:
        moto= Motos.objects.get (id=pk)
        moto.delete()
        context = {'mensaje':"La moto se ha eliminado correctamente"}
        return render(request,'motos.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'motos.html',context=context) 

def eliminar_camion (request,pk):
    try:
        camion= Camiones.objects.get (id=pk)
        camion.delete()
        context = {'mensaje':"El camion se ha eliminado correctamente"}
        return render(request,'camiones.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'camion.html',context=context)  



