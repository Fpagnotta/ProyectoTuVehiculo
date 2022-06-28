from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
from vehiculos.models import Cars,Motorcycles,Trucks
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


""" def list_car(request):
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
 """


# -------- CREATE ELEMENT --------
""" def create_car(LogiRequiredMixin,request):
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

 """

# ------- DETAIL ELEMENT -------
""" def car_details(request, pk):
    try:
        cars = Cars.objects.get(id=pk)
        context = {'cars': cars}
        return render(request,'car_details.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'cars.html',context=context)    

def motorcycle_details(request, pk):
    try:
        motorcycles = Motorcycles.objects.get(id=pk)
        context = {'motorcycles':motorcycles}
        return render(request,'motorcycles_details.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'motorcycles.html',context=context)    

def truck_details(request, pk):
    try:
        trucks = Trucks.objects.get(id=pk)
        context = {'trucks': trucks}
        return render(request,'trucks_details.html', context=context)
    except:
        context = {'problema':'Hay un problema en cargar este detalle, disculpe las molestias'}
        return render (request,'trucks.html',context=context)    
 """

# ------ DELETE ELEMENT -------
""" def delete_car (request,pk):
    try:
        car = Cars.objects.get (id=pk)
        car.delete()
        context = {'mensaje':"El auto se ha eliminado correctamente"}
        return render(request,'delete_car.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'delete_car.html',context=context)  

def delete_motorcycle (request,pk):
    try:
        motorcycle = Motorcycles.objects.get (id=pk)
        motorcycle.delete()
        context = {'mensaje':"La moto se ha eliminado correctamente"}
        return render(request,'delete_motorcycle.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'delete_motorcycle.html',context=context) 

def delete_truck (request,pk):
    try:
        truck = Trucks.objects.get (id=pk)
        truck.delete()
        context = {'mensaje':"El camion se ha eliminado correctamente"}
        return render(request,'delete_truck.html',context=context)
    except:
        context = {'problema':'Hay un problema en eliminar este vehiculo, disculpe las molestias'}
        return render (request,'delete_truck.html',context=context)  
 """





# ------- ELEMENT WITH CLASS--------
class list_car(ListView):
    model = Cars
    template_name = "list_car.html"
    queryset: Cars.objects.filter(is_active = True)

class list_motorcycle(ListView):
    model = Motorcycles
    template_name = "list_motorcycle.html"
    queryset: Motorcycles.objects.filter(is_active = True)

class list_truck(ListView):
    model = Trucks
    template_name = "list_truck.html"
    queryset: Trucks.objects.filter(is_active = True)



# -------- SEARCH ---------
def search_vehicle(request):
    print(request.GET)
    truck = Trucks.objects.filter(brand__contains = request.GET["Search"])
    car = Cars.objects.filter(brand__contains = request.GET["Search"])
    motorcycle = Motorcycles.objects.filter(brand__contains = request.GET["Search"])
    context = {"car": car, "truck": truck, "motorcycle": motorcycle}
    return render(request,"search_vehicle.html", context = context)


# --------- CREATE ELEMENT WITH CLASS ----
class create_car_view(LoginRequiredMixin,CreateView):
    model = Cars
    template_name = "create_car.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("car_details", kwargs={"pk": self.object.pk})

class create_motorcycle_view(LoginRequiredMixin,CreateView):
    model = Motorcycles
    template_name = "create_motorcycle.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("motorcycle_details", kwargs={"pk": self.object.pk})

class create_truck_view(LoginRequiredMixin,CreateView):
    model = Trucks
    template_name = "create_truck.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("truck_details", kwargs={"pk": self.object.pk})




# --------- DETAIL ELEMENT WITH CLASS ----
class detail_car_view(DetailView):
    model = Cars
    template_name = "details_car.html"
    
class detail_motorcycle_view(DetailView):
    model = Motorcycles
    template_name = "details_motorcycle.html"
    
class detail_truck_view(DetailView):
    model = Trucks
    template_name = "details_truck.html"
    
    
    
    
# ------- UPDATE ELEMENT WITH CLASS --------------
class update_car_view(LoginRequiredMixin,UpdateView):
    model = Cars
    template_name = "update_car.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("details_car.html", kwargs= {"pk": self.object.pk})

class update_motorcycle_view(LoginRequiredMixin,UpdateView):
    model = Motorcycles
    template_name = "update_motorcycle.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("details_motorcycle.html", kwargs= {"pk": self.object.pk})

class update_truck_view(LoginRequiredMixin,UpdateView):
    model = Trucks
    template_name = "update_truck.html"
    fields = "__all__"
    
    def get_success_url(self):
        return reverse("details_truck.html", kwargs= {"pk": self.object.pk})

# ------- DELETE ELEMENT WITH CLASS --------------
class delete_car_view(LoginRequiredMixin,DeleteView):
    model = Cars
    template_name = "delete_car.html"
    
    def get_success_url(self):
        return reverse("cars")
class delete_motorcycle_view(LoginRequiredMixin,DeleteView):
    model = Motorcycles
    template_name = "delete_motorcycle.html"
    
    def get_success_url(self):
        return reverse("motorcycles")
class delete_truck_view(LoginRequiredMixin,DeleteView):
    model = Trucks
    template_name = "delete_truck.html"
    
    def get_success_url(self):
        return reverse("trucks")