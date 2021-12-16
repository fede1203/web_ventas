from django.urls import path
from django.urls.resolvers import URLPattern
from AppVentas import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio' ),
    path('blancos', views.blancos, name='Blancos' ),
    path('cocinas', views.cocinas, name='Cocinas'),
    path('electrodomesticos', views.electrodomesticos, name='Electrodomesticos'),
    path('blan_form', views.blan_form, name="Blan_form"),
    path('cocinaFormulario', views.cocinaFormulario, name="CocinaFormulario"),
    path('electroFormulario', views.electroFormulario, name="ElectroFormulario"),
]