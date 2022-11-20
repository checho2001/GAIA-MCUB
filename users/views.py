from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from  users.forms import loginForm
from django.urls import reverse
from .models import User
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
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
			
def login(request):
    form = loginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            correo = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if 'usua_actual' in request.session:
                usuario_intentando = request.session['usua_actual']
            else:
                request.session['usua_actual'] = correo
                usuario_intentando = correo
				
            return HttpResponseRedirect(reversed('users:galery'))
            if usuario_intentando == correo:

                    user = auth.authenticate(email=correo, password=password)

                    if user is not None:
                        # Correct password, and the user is marked "active"
                        auth.login(request, user)
						
                        # Redirect to a success page.
                        return HttpResponseRedirect(reverse('registerUser.html'))
                   
    return render(request, 'login.html', {'form':form})
     

def register(request):

    if request.method == 'POST':
        form = CustomUser(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            rol = form.cleaned_data['rol']
            user = User(nombre= nombre, apellido = apellido , email = correo,rol=Rol.objects.get(id=rol),password=make_password(password))
            user.is_superuser = False
            user.is_staff = False
            user.is_active = False
            user.save()
           
    else:
        form = CustomUser()


    return render(request, 'registerUser.html', {'form':form})