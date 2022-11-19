from statistics import mode
from django.db import models

# Create your models here.

class Users(models.Model):
    UsersID = models.AutoField(primary_key=True)
   
    
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

