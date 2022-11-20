from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from  users.forms import loginForm
from .models import User
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
class IndexView(View):
        def get(self,request):
            return render(request,"index.html")
class Galry(View):
        def get(self,request):
            return render(request,"galery.html")
class Dashboard(View):
        def get(self,request):
            return render(request,"dashboard.html")			
			
def login(request):
    formulario = loginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['username']
            pass
    return render(request,"login.html",{'form':formulario})  


def register(request):

    if request.method == 'POST':
        form = CustomUser(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            rol = form.cleaned_data['rol']
            

            user = User(nombre= nombre, apellido = apellido ,email = correo,rol=Rol.objects.get(id=rol))
            user.is_superuser = False
            user.is_staff = False
            user.is_active = False
            user.save()
           
    else:
        form = CustomUser()


    return render(request, 'registerUser.html', {'form':form})