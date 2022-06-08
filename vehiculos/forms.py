from django import forms

class Autos_form(forms.Form):
    marca_modelo = forms.CharField (max_length=50)
    año = forms.FloatField()
    transmision = forms.BooleanField()
    sku = forms.CharField(max_length=30)
    precio = forms.FloatField()
    
class Camiones_form(forms.Form):
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
    precio = forms.FloatField()