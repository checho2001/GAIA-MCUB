from statistics import mode
from django.db import models

# Create your models here.
class Users(models.Model):
 
   correo= models.CharField(max_length=50)
   contrasenia= models.CharField(max_length=50)
   contrasenia2= models.CharField(max_length=50)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

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
    FechaEvento = models.DateTimeField(max_length=500)
    Habitad= models.CharField(max_length=500)
    Departamento= models.CharField(max_length=500)
    Municipio= models.CharField(max_length=500)
    IdentificadoPor= models.CharField(max_length=500)
    FechaIdentificacion = models.DateTimeField(max_length=500)
    IdentificacionReferencias = models.CharField(max_length=500)
    ComentarioIdentificacion = models.CharField(max_length=500)
    NombreCientificoComentarioRegistroBiologico = models.CharField(max_length=500)
    Clase = models.CharField(max_length=500)
    Orden = models.CharField(max_length=500)
    Familia = models.CharField(max_length=500)
    Genero = models.CharField(max_length=500)
    NombreComun = models.CharField(max_length=500)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['email', 'password']

