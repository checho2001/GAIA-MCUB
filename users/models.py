from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
   
    
 

class Rol(models.Model):
    idrol=models.IntegerField()
    nombrerol = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

class Especimen(models.Model):
    NumeroCatalogo = models.CharField(max_length=500)
    NombreDelConjuntoDatos = models.CharField(max_length=500)
    ComentarioRegistroBiologico = models.CharField(max_length=500)
    RegistradoPor = models.CharField(max_length=500)
    NumeroIndividuo = models.IntegerField()
    FechaEvento = models.DateTimeField()
    Habitad= models.CharField(max_length=500)
    Departamento= models.CharField(max_length=500)
    Municipio= models.CharField(max_length=500)
    IdentificadoPor= models.CharField(max_length=500)
    FechaIdentificacion = models.DateTimeField()
    IdentificacionReferencias = models.CharField(max_length=500)
    ComentarioIdentificacion = models.CharField(max_length=500)
    NombreCientificoComentarioRegistroBiologico = models.CharField(max_length=500)
    Clase = models.CharField(max_length=500)
    Orden = models.CharField(max_length=500)
    Familia = models.CharField(max_length=500)
    Genero = models.CharField(max_length=500)
    NombreComun = models.CharField(max_length=500)
    USERNAME_FIELD='NumeroCatalogo'
    REQUIRED_FIELDS = ['NumeroCatalogo', 'NombreDelConjuntoDatos',]

