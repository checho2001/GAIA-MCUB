from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.core.validators import RegexValidator
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
    estado = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def group_defined():
        if(Rol.id == 1):
            grupo = Group.objects.get_or_create(name='Auxiliar')
        if(Rol.id == 2):
            grupo2 = Group.objects.get_or_create(name='Pasante')

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
    TareaRealizada = models.ForeignKey(TipoActividad,on_delete=models.CASCADE)
    Hora = models.TimeField(max_length=50)
    Fecha = models.DateField(max_length=50)
    Descripcion = models.CharField(max_length=1000)
 
    def __str__(self):
        return self.TareaRealizada

class departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre= models.CharField( max_length=50)
class municipio(models.Model):
    id = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(departamento,on_delete=models.CASCADE)
    municipio= models.CharField(max_length=50) 
class especimen(models.Model):
    id = models.AutoField(primary_key=True)
    NumeroCatalogo = models.CharField(max_length=500)
    NombreDelConjuntoDatos = models.CharField(max_length=500)
    ComentarioRegistroBiologico = models.CharField(max_length=500)
    RegistradoPor = models.CharField(max_length=500)
    NumeroIndividuo = models.CharField(max_length=500)
    FechaEvento = models.DateField(blank=True,null=True,max_length=500)
    Habitad= models.CharField(max_length=500)
    Departamento = models.CharField(max_length=500)
    Municipio= models.CharField(max_length=500)
    IdentificadoPor= models.CharField(max_length=500)
    FechaIdentificacion = models.DateField(max_length=500)
    IdentificacionReferencias = models.CharField(max_length=500)
    ComentarioIdentificacion = models.CharField(max_length=500)
    NombreCientificoComentarioRegistroBiologico = models.CharField(max_length=500)
    ClaseE =   models.CharField(max_length=500)
    Orden =   models.CharField(max_length=500)
    Genero =   models.CharField(max_length=500)
    Familia =   models.CharField(max_length=500)
    NombreComun = models.CharField(max_length=500)
    Image = models.ImageField(upload_to="ejemplares", null=True)

    def __str__(self):
        return (self.NumeroCatalogo)  
    def clean(self):
        super().clean()

        if not self.FechaEvento:
            return
class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarea = models.CharField(max_length=100)
    ejemplar = models.CharField(max_length=100)
    tiempo = models.DateTimeField(auto_now_add=True)