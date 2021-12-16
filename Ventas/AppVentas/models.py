from django.db import models

class Blancos(models.Model):
    marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    color = models.CharField(max_length=30)
    plazas = models.IntegerField()
    precio = models.IntegerField()

class Cocinas(models.Model):
    marca = models.CharField(max_length=60)
    color = models.CharField(max_length=30)    
    canti_hornallas = models.IntegerField()
    
class Electrodomesticos(models.Model):
    tipo = models.CharField(max_length=60) 
    marca = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    color = models.CharField(max_length=30) 
    voltage = models.IntegerField() 




