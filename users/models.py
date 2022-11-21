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

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=50)
    def __str__(self):
        return self.nombreGenero     
    
class Familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombreFamilia = models.CharField(max_length=50)
    genero= models.ForeignKey(Genero,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreFamilia 
class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    nombreOrden = models.CharField(max_length=50)
    familia= models.ForeignKey(Familia,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreOrden
    
class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    nombreClase = models.CharField(max_length=50)
    ordern= models.ForeignKey(Orden,on_delete=models.CASCADE)
   
    
    def __str__(self):
        return self.nombreClase
           

class TipoActividad(models.Model):
    id = models.AutoField(primary_key=True)
    nombreactividad = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.nombreactividad
class Actividades(models.Model):
    id = models.AutoField(primary_key=True)
    NumeroCatalogo = models.CharField(max_length=50)
    TareaRealizada = models.CharField(max_length=50)
    Hora = models.CharField(max_length=50)
    Fecha = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=500)
 
    def __str__(self):
        return self.TareaRealizada

class Ejemplar(models.Model):
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
    Clase =  models.ForeignKey(Clase,on_delete=models.CASCADE)
    NombreComun = models.CharField(max_length=500)
   
    
    def __str__(self):
        return self.NumeroCatalogo        