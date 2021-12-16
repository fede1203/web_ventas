from django.conf.urls import url
from django.http.response import HttpResponse
from django.shortcuts import render
from AppVentas.models import *




def blan_form(request):

    if request.method == "POST":
        blanco_insta = Blancos(request.POST["marca"], request.POST["descripcion"], request.POST["color"], request.POST["plazas"],request.POST["precio"])

        blanco_insta.save()

        return render(request, 'AppVentas/inicio.html')




    return render(request,"AppVentas/blan_form.html") 



def cocinaFormulario(request):

    if request.method == "POST":
        cocina_insta = Cocinas(request.POST["marca"], request.POST["color"], request.POST["canti_hornallas"])

        cocina_insta.save()

        return render(request, 'AppVentas/inicio.html')




    return render(request,"AppVentas/cocinaFormulario.html") 



def electroFormulario(request):

    if request.method == "POST":
        blanco_insta = Electrodomesticos(request.POST["marca"], request.POST["descripcion"],request.POST["modelo"], request.POST["color"], request.POST["voltage"])

        blanco_insta.save()

        return render(request, 'AppVentas/inicio.html')




    return render(request,"AppVentas/electroFormulario.html")     



def inicio(request):
    return render(request,"AppVentas/inicio.html")


def blancos(request):
    return render(request,"AppVentas/blancos.html")

def cocinas(request):
    return render(request,"AppVentas/cocinas.html") 


def electrodomesticos(request):
    return render(request,"AppVentas/electrodomesticos.html")    


     