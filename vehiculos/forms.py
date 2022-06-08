from django import forms
from vehiculos.models import Autos, Camiones, Motos

""" class Autos_form(forms.Form):
    marca_modelo = forms.CharField (max_length=50)
    año = forms.FloatField()
    transmision = forms.BooleanField()
    sku = forms.CharField(max_length=30)
    precio = forms.FloatField() """

""" class Camiones_form(forms.Form):
    marca_modelo = forms.CharField (max_length=50)
    año = forms.FloatField()
    capacidad = forms.CharField(max_length=30)
    sku = forms.CharField (max_length=30)
    precio = forms.FloatField ()
    
class Motos_form(forms.Form):
    marca_modelo = forms.CharField(max_length=50)
    año = forms.FloatField()
    tipo = forms.CharField(max_length=20)
    sku = forms.CharField(max_length=30)
    precio = forms.FloatField() """

class Autos_form(forms.ModelForm):
    class Meta:
        model = Autos
        fields = "__all__"
    
class Camiones_form(forms.ModelForm):
    class Meta:
        model = Camiones
        fields = "__all__"

class Motos_form(forms.ModelForm):
    class Meta:
        model = Motos
        fields = "__all__"
    