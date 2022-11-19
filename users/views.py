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
   