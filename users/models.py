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
    UsersID = models.CharField(max_length=500)
    Registradopor = models.CharField(max_length=500)
    Ocurrencias = models.CharField(max_length=500)
    Departamento = models.CharField(max_length=500)
    Municipio = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    estado= models.BooleanField(default=False)
   
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['email', 'password']

