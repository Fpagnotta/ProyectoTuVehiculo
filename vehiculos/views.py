from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import UpdateView
from vehiculos.models import Cars,Motorcycles,Trucks
from vehiculos.forms import Car_form, Truck_form, Motorcycle_form

# Create your views here.


def list_car(request):
    cars= Cars.objects.all()
    context={'cars':cars}
    return render(request,'cars.html',context=context)

def list_motorcycle(request):
    motorcycles = Motorcycles.objects.all()                          
    context={'motorcycles':motorcycles}
    return render(request,'motorcycles.html',context=context)

def list_truck(request):
    trucks = Trucks.objects.all()        
    context= {'trucks': trucks}
    return render(request,'trucks.html',context=context)



# -------- CREATE ELEMENT --------
def create_car(request):
    if request.method == "GET":
        form = Car_form()
        context = {"form":form}
        return render (request,'create_car.html',context=context)
    else:
        form = Car_form(request.POST)
        if form.is_valid():
            new_car = Cars.objects.create(
                 brand = form.cleaned_data["brand"],
                 year = form.cleaned_data["year"],
                 transmision = form.cleaned_data["transmision"],
                 sku = form.cleaned_data["sku"],
                 price = form.cleaned_data["price"],
            )
            context = {"new_car":new_car}
        return render (request,'create_car.html',context=context)

def create_truck(request):
    if request.method == "GET":
        form = Truck_form()
        context = {"form":form}
        return render (request,'create_truck.html',context=context)
    else:
        form = Truck_form(request.POST)
        if form.is_valid():
            new_truck = Trucks.objects.create(
                 brand = form.cleaned_data["brand"],
                 year = form.cleaned_data["year"],
                 capacity = form.cleaned_data["capacity"],
                 sku = form.cleaned_data["sku"],
                 price = form.cleaned_data["price"],
            )
            context = {"new_truck":new_truck}
        return render (request,'create_truck.html',context=context)
 
def create_motorcycle(request):
    if request.method == "GET":
        form = Motorcycle_form()
        context = {"form":form}
        return render (request,'create_motorcycle.html',context=context)
    else:
        form = Motorcycle_form(request.POST)
        if form.is_valid():
            new_motorcycle = Motorcycles.objects.create(
                 brand = form.cleaned_data["brand"],
                 year = form.cleaned_data["year"],
                 type = form.cleaned_data["type"],
                 sku = form.cleaned_data["sku"],
                 price = form.cleaned_data["price"],
            )
            context = {"new_motorcycle":new_motorcycle}
        return render (request,'create_motorcycle.html',context=context)


# -------- SEARCH ---------
def search_vehicle(request):
    print(request.GET)
    truck = Trucks.objects.filter(brand__contains = request.GET["Search"])
    car = Cars.objects.filter(brand__contains = request.GET["Search"])
    motorcycle = Motorcycles.objects.filter(brand__contains = request.GET["Search"])
    context = {"car": car, "truck": truck, "motorcycle": motorcycle}
    return render(request,"search_vehicle.html", context = context)


# ------- DETAIL ELEMENT -------
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


# ------ DELETE ELEMENT -------
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

# ------- UPDATE ELEMENT -----
class update_vehicle(UpdateView):
    model = Cars, Motorcycles, Trucks
    template_name = "update_vehicle.html"
    fields = ["price"]
    
    def get_success_url(self):
        return reverse("autos_detalles.html", "motos_detalles.html", "camiones_detalles.html", kwargs= {"pk": self.object.pk})