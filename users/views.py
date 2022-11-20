from django.shortcuts import render

from django.views import View
from django.contrib.auth import login
from users.forms import *
from  users.forms import loginForm
from .models import Users
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registerUser.html", context={"register_form":form})
   