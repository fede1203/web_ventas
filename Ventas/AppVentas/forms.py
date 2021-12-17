from django import forms

class BlancoFormulario(forms.Form):
    marca = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30)
    plazas = forms.IntegerField()
    precio = forms.IntegerField()


class CocinaFormulario(forms.Form):
    marca = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30)    
    canti_hornallas = forms.IntegerField()
    
class ElectrodomesticosFormulario(forms.Form):
    tipo = forms.CharField(max_length=60) 
    marca = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=60)
    modelo = forms.CharField(max_length=60)
    color = forms.CharField(max_length=30) 
    voltage = forms.IntegerField()    