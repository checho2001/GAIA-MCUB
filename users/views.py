from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from  users.forms import loginForm
from django.urls import reverse
from .models import User, Actividades, TipoActividad
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
class IndexView(View):
        def get(self,request):
            return render(request,"index.html")
class Galry(View):
        def get(self,request):
            return render(request,"galery.html")
class Dashboard(View):
        def get(self,request):
            return render(request,"dashboard.html")	
class PerfilU(View):
        def get(self,request):
            return render(request,"profile.html")		            		
			
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
    else:
        form = ActividadesForm()
    return render(request, 'informe1.html', {'form':form})
    