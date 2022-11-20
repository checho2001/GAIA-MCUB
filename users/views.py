from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.views import View
from django.contrib import auth
from django.urls import reverse   
from django.contrib.auth import login, authenticate  # add to imports
from users.forms import *
from  users.forms import loginForm
from .models import Users
from .forms import loginForm

class IndexView(View):
        def get(self,request):
            return render(request,"index.html")

def login(request):
    formulario = loginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['username']
            pass
    return render(request,"login.html",{'form':formulario})  


def registro(request):

    if request.method == 'POST':
        form = registerUserForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            rol = form.cleaned_data['rol']
            

            username=correo
           

            return render(request, 'index.html', {'msg':'Hemos enviado a tu correo un token de verificacion, por favor revisalo para verificar tu correo electronico y emepzar a disfrutar de nuestros servicios'})
    
    else:
        form = registerUserForm()


    return render(request, 'Register.html', {'form':form})
   