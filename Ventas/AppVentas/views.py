from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render
from AppVentas.models import *
from AppVentas.forms import *




def blan_form(request):

    if request.method == "POST":

        miFormulario = BlancoFormulario(request.POST)

        if miFormulario.is_valid():
             
            informacion = miFormulario.cleaned_data

            blanco_insta = blanco_insta = Blancos(marca=informacion["marca"], descripcion=informacion["descripcion"], color=informacion["color"], plazas=informacion["plazas"],precio=informacion["precio"])

            blanco_insta.save()

            return render(request, 'AppVentas/inicio.html')

    else:
        miFormulario = BlancoFormulario()


    return render(request,"AppVentas/blan_form.html", {'miFormulario':miFormulario})    


def cocinaFormulario(request):

    if request.method == "POST":
        miFormulario = CocinaFormulario(request.POST)

        if miFormulario.is_valid():
           informacion = miFormulario.cleaned_data

        cocina_insta = Cocinas(marca = informacion["marca"], color=informacion["color"], canti_hornallas=informacion["canti_hornallas"])

        cocina_insta.save()

        return render(request, 'AppVentas/inicio.html')
    else:
        miFormulario = CocinaFormulario()

    return render(request,"AppVentas/cocinaFormulario.html", {'miFormulario':miFormulario}) 


def electroFormulario(request):

    if request.method == "POST":
        miFormulario = ElectrodomesticosFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        blanco_insta = Electrodomesticos(marca=informacion["marca"], descripcion=informacion["descripcion"],modelo=informacion["modelo"], color=informacion["color"], voltage=informacion["voltage"])

        blanco_insta.save()

        return render(request, 'AppVentas/inicio.html')
    else:
        miFormulario = ElectrodomesticosFormulario()



    return render(request,"AppVentas/electroFormulario.html", {'miFormulario': miFormulario})     



def inicio(request):
    return render(request,"AppVentas/inicio.html")


def blancos(request):
    return render(request,"AppVentas/blancos.html")

def cocinas(request):
    return render(request,"AppVentas/cocinas.html") 


def electrodomesticos(request):
    return render(request,"AppVentas/electrodomesticos.html")    


     