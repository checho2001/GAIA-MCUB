from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.views import View
from django.contrib import auth
from django.urls import reverse   


class IndexView(View):
        def get(self,request):
            return render(request,"index.html")
