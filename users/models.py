from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.core.validators import RegexValidator
from .fields import ActionField

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.nombrerol
class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    rol= models.ForeignKey(Rol,on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def group_defined():
        if(Rol.id == 1):
            grupo = Group.objects.get_or_create(name='Auxiliar')
        if(Rol.id == 2):
            grupo2 = Group.objects.get_or_create(name='Pasante')

class Area_User(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_area = models.ForeignKey(Area,on_delete=models.CASCADE)

class Genero(models.Model):
    id = models.AutoField(primary_key=True)
    nombreGenero = models.CharField(max_length=50)
    def __str__(self):
        return self.nombreGenero     
    
class familia(models.Model):
    id = models.AutoField(primary_key=True)
    nombreFamilia = models.CharField(max_length=50)
   
    
    def __str__(self):
        return self.nombreFamilia 
class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    nombreOrden = models.CharField(max_length=50)
 
    
    def __str__(self):
        return self.nombreOrden
    
class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    nombreClase = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    
    def __str__(self):
        return self.nombreClase
    
class Class_User(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_clase = models.ForeignKey(Clase,on_delete=models.CASCADE)
           
class TipoActividad(models.Model):
    id = models.AutoField(primary_key=True)
    nombreactividad = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)
   
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
    NumeroCatalogo = models.CharField(max_length=500, unique= True)
    NombreDelConjuntoDatos = models.CharField(max_length=500)
    ComentarioRegistroBiologico = models.CharField(max_length=500)
    RegistradoPor = models.CharField(max_length=500)
    NumeroIndividuo = models.CharField(max_length=500)
    FechaEvento = models.DateField(max_length=500,blank=True,null=True,)
    Habitad= models.CharField(max_length=500)
    Departamento = models.CharField(max_length=500)
    Municipio= models.CharField(max_length=500)
    IdentificadoPor= models.CharField(max_length=500)
    FechaIdentificacion = models.DateField(max_length=500,blank=True,null=True)
    IdentificacionReferencias = models.CharField(max_length=500)
    ComentarioIdentificacion = models.CharField(max_length=500)
    NombreCientificoComentarioRegistroBiologico = models.CharField(max_length=500)
    ClaseE =   models.CharField(max_length=500)
    Orden =   models.CharField(max_length=500)
    Genero =   models.CharField(max_length=500)
    Familia =   models.CharField(max_length=500)
    NombreComun = models.CharField(max_length=500)
    estado = models.BooleanField(default=True)
    Image = models.ImageField(upload_to='media/')

    def __str__(self):
        return (self.NumeroCatalogo)  
    
class UserAction(models.Model):
    id_user_action = ActionField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tarea = models.CharField(max_length=100)
    ejemplar = models.CharField(max_length=100)
    tiempo = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)

class Imagenes(models.Model):
    image = models.ImageField(upload_to='media/')
