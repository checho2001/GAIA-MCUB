from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.nombrerol

class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    rol= models.ForeignKey(Rol,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


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
    class Meta:
       managed = False
       db_table = 'Especimenes'

