from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from  users.forms import loginForm
from django.urls import reverse
from .models import User, Actividades, TipoActividad,Clase,especimen,UserAction
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
class IndexView(View):
        def get(self,request):
            return render(request,"index.html")
class CambioContrasenia(View):
        def get(self,request):
            return render(request,"changepassword.html")
class Galry(View):
        def get(self,request):
            return render(request,"galery.html")
          
class Dashboard(View):  
        def get(self,request):
            actions = UserAction.objects.filter(user=request.user).order_by('tiempo')
            print("acciones", actions)
            return render(request,"dashboard.html",{'actions': actions})
                	
class PerfilU(View):
        def get(self,request):
            return render(request,"profile.html")		            		
class EjemplarP(View):
        def get(self,request):
            return render(request,"paginaejemplar.html")		            		
						
def login(request):
    form = loginForm(request.POST) 
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user is not  None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
                   
    return render(request, 'login.html', {'form':form})
     
@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            rol = form.cleaned_data['rol']
            user = User(username=username,nombre= nombre, apellido = apellido , email = correo,rol=Rol.objects.get(id=rol),password=make_password(password))
            print(user)
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()
            
    else:
        form = CustomUser()
    return render(request, 'registerUser.html', {'form':form})


class registro(View):
        def get(self,request):
            return render(request,"register.html")
@login_required           
def registroActividad(request):
    form = ActividadesForm(request.POST)
    if request.method == 'POST':
     
        if form.is_valid():
            NumeroCatalogo = form.cleaned_data['NumeroCatalogo']
            TareaRealizada = form.cleaned_data['TareaRealizada']
            Hora = form.cleaned_data['Hora']
            Fecha = form.cleaned_data['Fecha']
            Descripcion = form.cleaned_data['Descripcion']
            a = Actividades(NumeroCatalogo=NumeroCatalogo,TareaRealizada= TipoActividad.objects.get(id=TareaRealizada), Hora = Hora , Fecha = Fecha,Descripcion=Descripcion)   
            a.save()
            UserAction.objects.create(user=request.user, tarea=form.cleaned_data['TareaRealizada'],ejemplar= form.cleaned_data['NumeroCatalogo'])
    else:
        form = ActividadesForm()
    return render(request, 'informe1.html', {'form':form})

@login_required 
def registerE(request):
    if request.method == 'POST':
        form = EjemplarForm(request.POST)
        if form.is_valid():
            NumeroCatalogo = form.cleaned_data['NumeroCatalogo']
            NombreDelConjuntoDatos = form.cleaned_data['NombreDelConjuntoDatos']
            ComentarioRegistroBiologico = form.cleaned_data['ComentarioRegistroBiologico']
            RegistradoPor = form.cleaned_data['RegistradoPor']
            NumeroIndividuo = form.cleaned_data['NumeroIndividuo']
            FechaEvento = form.cleaned_data['FechaEvento']
            Habitad = form.cleaned_data['Habitad']
            Departamento = form.cleaned_data['Departamento']
            Municipio = form.cleaned_data['Municipio']
            IdentificadoPor = form.cleaned_data['IdentificadoPor']
            FechaEvento = form.cleaned_data['FechaEvento']
            FechaIdentificacion = form.cleaned_data['FechaIdentificacion']
            IdentificacionReferencias = form.cleaned_data['FechaEvento']
            ComentarioIdentificacion = form.cleaned_data['ComentarioIdentificacion']
            NombreCientificoComentarioRegistroBiologico = form.cleaned_data['NombreCientificoComentarioRegistroBiologico']
            ClaseE = form.cleaned_data['ClaseE']
            NombreComun = form.cleaned_data['NombreComun']
           
            e = especimen(NumeroCatalogo=NumeroCatalogo,NombreDelConjuntoDatos= NombreDelConjuntoDatos, ComentarioRegistroBiologico = ComentarioRegistroBiologico 
            , RegistradoPor = RegistradoPor,NumeroIndividuo=NumeroIndividuo,FechaEvento=FechaEvento,Habitad=Habitad,Departamento=Departamento.objects.get(id=Departamento),Municipio=Municipio.objects.get(id=Municipio)
            ,IdentificadoPor=IdentificadoPor,FechaIdentificacion=FechaIdentificacion,IdentificacionReferencias=IdentificacionReferencias,ComentarioIdentificacion=ComentarioIdentificacion,
            NombreCientificoComentarioRegistroBiologico=NombreCientificoComentarioRegistroBiologico,ClaseE=Clase.objects.get(id=ClaseE),NombreComun=NombreComun)
            e.save()
            
    else:
        form = EjemplarForm()
    return render(request, 'registerE.html', {'form':form})    



@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")