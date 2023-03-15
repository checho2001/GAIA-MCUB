from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from  users.forms import loginForm
from django.urls import reverse
from .models import User, Actividades, TipoActividad,Clase,especimen,UserAction, departamento, municipio,familia,Genero,Orden, Area_User
from .forms import loginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from django.shortcuts import render, get_object_or_404
from datetime import datetime


class IndexView(View):
        def get(self,request):
            return render(request,"index.html")
class Not_Logged(View):
        def get(self,request):
            return render(request,"notloged.html")            
class CambioContrasenia(View):
        def get(self,request):
            return render(request,"changepassword.html")
class Galry(View):
        def get(self,request):
            especimenes = especimen.objects.all()
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
           
                
            return render(request,"galery.html",{'especimenes':especimenes,'familias':familias,'ordenes':ordenes,'clases':clases,'generos':generos})
def galery_familia(request,nombre):
            especimenes = especimen.objects.filter(Familia = nombre)
            familias =  familia.objects.filter(nombreFamilia = nombre)
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
            return render(request,"galery_filter.html",{'especimenes':especimenes,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_genero(request,nombre):
            especimenes = especimen.objects.filter(Genero = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.filter(nombreGenero = nombre)
            return render(request,"galery_filter.html",{'especimenes':especimenes,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_clase(request,nombre):
            especimenes = especimen.objects.filter(ClaseE = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.filter(nombreClase = nombre)
            generos =  Genero.objects.all()
            return render(request,"galery_filter.html",{'especimenes':especimenes,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_orden(request,nombre):
            especimenes = especimen.objects.filter(Orden = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.filter(nombreOrden = nombre)
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
            return render(request,"galery_filter.html",{'especimenes':especimenes,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})
 
class Dashboard_Aux(View):
        def get(self,request):
            actions = UserAction.objects.filter(user=request.user).order_by('tiempo')
            especimenes = especimen.objects.all()
            return render(request,"dashauxiliar.html",{'especimenes':especimenes,'actions':actions})
class Dashboard_Pas(View):
        def get(self,request):
            return render(request,"dashpasante.html")
class Dashboard_Cur(View):
        def get(self,request):
            area = Area_User.objects.get(id_user_id= request.user.id )
            a = Area_User.objects.filter(id_area_id=area.id_area_id)
            lista = []
            for i in a:
                lista.append(i.id_user_id)
            especimenes = especimen.objects.all()
            actions = UserAction.objects.filter(user__in = lista)
            return render(request,"dashcurador.html",{'actions': actions, 'especimenes':especimenes})
          
class Dashboard(View):
        @method_decorator(login_required(login_url='redirect')   ) 
        def get(self,request):
            especimenes = especimen.objects.all()
            actions = UserAction.objects.order_by('tiempo').all()
            return render(request,"dashboard.html",{'especimenes':especimenes,'actions': actions})
                	
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
   
            if user is not  None:
                auth.login(request, user)
                if user.groups.filter(name__in=['Auxiliar']):
                    
                    return HttpResponseRedirect(reverse('dashboardAux'))
                if user.groups.filter(name__in=['Pasante']):
                   
                    return HttpResponseRedirect(reverse('dashboardPas'))
                if user.groups.filter(name__in=['Curador']):
                    
                    return HttpResponseRedirect(reverse('dashboardCur'))
                return HttpResponseRedirect(reverse('dashboard'))
                   
    return render(request, 'login.html', {'form':form})
     
@login_required(login_url='redirect')
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
           
            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()
         
            if(rol == "1"):
             
                group = Group.objects.get(name='Auxiliar')
                group.user_set.add(user)
            elif(rol == "2"):
                group = Group.objects.get(name='Pasante')
                group.user_set.add(user)
            elif(rol == "3"):
                group = Group.objects.get(name='Curador')
                group.user_set.add(user)
            elif(rol == "4"):
                group = Group.objects.get(name='Otro')
                group.user_set.add(user)
            area = form.cleaned_data['area']
            area_user = Area_User(id_user = User.objects.get(id=user.id), id_area = Area.objects.get(id=area))
            area_user.save()
    else:
        form = CustomUser()
    return render(request, 'registerUser.html', {'form':form})

@login_required(login_url='redirect')
def registroActividad(request):
    form = ActividadesForm(request.POST)
    if request.method == 'POST':
     
        if form.is_valid():
            NumeroCatalogo = form.cleaned_data['NumeroCatalogo']
            TareaRealizada = form.cleaned_data['TareaRealizada']
            Hora = form.cleaned_data['Hora']
            Fecha = form.cleaned_data['Fecha']
            Descripcion = form.cleaned_data['Descripcion']
            a = Actividades(NumeroCatalogo=especimen.objects.get(id=NumeroCatalogo),TareaRealizada= TipoActividad.objects.get(id=TareaRealizada), Hora = Hora , Fecha = Fecha,Descripcion=Descripcion)   
            a.save()
            userAction = UserAction(user=request.user, tarea= TipoActividad.objects.get(id=TareaRealizada),ejemplar= especimen.objects.get(id=NumeroCatalogo))
            userAction.save()
    else:
        form = ActividadesForm()
    return render(request, 'informe1.html', {'form':form})


@login_required(login_url='redirect')
def registerE(request):
    if request.method == 'POST':
        form = EjemplarForm(request.POST, request.FILES)
        
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
            Orden = form.cleaned_data['Orden']
            Genero = form.cleaned_data['Genero']
            Familia = form.cleaned_data['Familia']
            NombreComun = form.cleaned_data['NombreComun']

            e = especimen(NumeroCatalogo=NumeroCatalogo,NombreDelConjuntoDatos= NombreDelConjuntoDatos, ComentarioRegistroBiologico = ComentarioRegistroBiologico 
            , RegistradoPor = RegistradoPor,NumeroIndividuo=NumeroIndividuo,FechaEvento=FechaEvento,Habitad=Habitad,Departamento=departamento.objects.get(id=Departamento),Municipio=municipio.objects.get(id=Municipio)
            ,IdentificadoPor=IdentificadoPor,FechaIdentificacion=FechaIdentificacion,IdentificacionReferencias=IdentificacionReferencias,ComentarioIdentificacion=ComentarioIdentificacion,
            NombreCientificoComentarioRegistroBiologico=NombreCientificoComentarioRegistroBiologico,ClaseE=Clase,Orden = Orden, Genero = Genero
            ,Familia = Familia, NombreComun=NombreComun , Image = "")
            e.save()
    else:
        form = EjemplarForm()
    return render(request, 'registerE.html', {'form':form}) 
   
@login_required(login_url='redirect')
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

class update_ejemplar(View):
        def get(self,request,id):
            ejemplar = especimen.objects.get(pk=id)
            contexto = {
                'id':ejemplar.id,
                'numeroCatalogo': ejemplar.NumeroCatalogo,
                'nombreDelConjuntoDatos' : ejemplar.NombreDelConjuntoDatos,
                'comentarioRegistro': ejemplar.ComentarioRegistroBiologico,
                'registrado': ejemplar.RegistradoPor,
                'numeroIndividuo': ejemplar.NumeroIndividuo,
                'fechaEvento': ejemplar.FechaEvento,
                'habitad': ejemplar.Habitad,
                'departamento': ejemplar.Departamento,
                'municipio': ejemplar.Municipio,
                'identificadoPor' : ejemplar.IdentificadoPor,
                'fechaIdentificacion': ejemplar.FechaIdentificacion,
                'identificacionReferencias' : ejemplar.IdentificacionReferencias,
                'comentarioIdentificacion' : ejemplar.ComentarioIdentificacion,
                'nombreCientifico' : ejemplar.NombreCientificoComentarioRegistroBiologico,
                'clase' : ejemplar.ClaseE,
                'nombreComun' : ejemplar.NombreComun,
            }
            
            return render(request,"updateE.html",{'contexto':contexto})

def update_record_ejemplar(request,id):

    numero = request.POST['NumeroCatalogo']
    nombredeDatos = request.POST['NombreDelConjuntoDatos']
    comentarioRegistro = request.POST['ComentarioRegistroBiologico']
    registradoPor = request.POST['RegistradoPor']
    numeroIndividuo = request.POST['NumeroIndividuo']
    
    habitad = request.POST['Habitad']
    departamento = request.POST['Departamento']
    municipio = request.POST['Municipio']
    identificadoPor = request.POST['IdentificadoPor']  
    idetificacionReferencias = request.POST['IdentificacionReferencias']
    comentarioIdentificacion = request.POST['ComentarioIdentificacion']
    nombreCientifico = request.POST['NombreCientifico']
    clase = request.POST['Clase']
    nombreComun = request.POST['NombreComun']
    ejemplar = especimen.objects.get(pk=id)
    ejemplar.NumeroCatalogo = numero
    ejemplar.NombreDelConjuntoDatos = nombredeDatos
    ejemplar.ComentarioRegistroBiologico = comentarioRegistro
    ejemplar.RegistradoPor = registradoPor
    ejemplar.NumeroIndividuo = numeroIndividuo
   
    ejemplar.Habitad = habitad
    ejemplar.Departamento = departamento
    ejemplar.Municipio = municipio
    ejemplar.IdentificadoPor = identificadoPor
 
    ejemplar.IdentificacionReferencias = idetificacionReferencias
    ejemplar.ComentarioIdentificacion = comentarioIdentificacion
    ejemplar.NombreCientificoComentarioRegistroBiologico = nombreCientifico
    ejemplar.ClaseE = clase
    ejemplar.NombreComun = nombreComun
    ejemplar.save()
    if request.user.groups.filter(name__in=['Auxiliar']):
        return HttpResponseRedirect(reverse('dashboardAux'))
    if request.user.groups.filter(name__in=['Pasante']):
        return HttpResponseRedirect(reverse('dashboardPas'))
    if request.user.groups.filter(name__in=['Curador']):
        return HttpResponseRedirect(reverse('dashboardCur'))
    return HttpResponseRedirect(reverse('dashboard'))


@login_required(login_url='redirect')
def update_aux(request):
    group = Group.objects.get(name="Auxiliar")
    users = User.objects.filter(groups__name="Auxiliar")
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            rol = form.cleaned_data['rol']
            user = username=User.objects.get(id=username)
            user.nombre=nombre
            user.apellido= apellido
            user.email=correo
            user.rol=Rol.objects.get(id=rol)
            user.save()
            
    else:
        form = Update()
    return render(request, 'UpdateUser.html', {'form':form})
@login_required(login_url='redirect')
def update_aux_curatoria(request):
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            rol = form.cleaned_data['rol']
            user = username=User.objects.get(id=username)
            user.nombre=nombre
            user.apellido= apellido
            user.email=correo
            user.rol=Rol.objects.get(id=rol)
            user.save()
            
    else:
        form = Update()
    return render(request, 'UpdateUser.html', {'form':form})    
@login_required(login_url='redirect')
def update_pasante(request):
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            rol = form.cleaned_data['rol']
            user = username=User.objects.get(id=username)
            user.nombre=nombre
            user.apellido= apellido
            user.email=correo
            user.rol=Rol.objects.get(id=rol)
            user.save()
            
    else:
        form = Update()
    return render(request, 'UpdateUser.html', {'form':form})    
@login_required(login_url='redirect')
def update_curador(request):
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            rol = form.cleaned_data['rol']
            user = username=User.objects.get(id=username)
            user.nombre=nombre
            user.apellido= apellido
            user.email=correo
            user.rol=Rol.objects.get(id=rol)
            user.save()
            
    else:
        form = Update()
    return render(request, 'UpdateUser.html', {'form':form})    
def load_data(request):
    root = tk.Tk()
    root.withdraw()

   
    file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    
    data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1],usecols=['catalogNumber', 'datasetName', 'occurrenceRemarks', 'recordedBy', 'individualCount',
                                              'eventDate', 'habitat', 'stateProvince', 'county', 'identifiedBy',  'dateIdentified',
                                                'identificationReferences', 'identificationRemarks', 'scientificName', 'class', 'order', 'family', 'genus', 
                                                'vernacularName'])
    
    for _, row in data.iterrows():
        if not pd.isnull(row['eventDate']):
            try:
                event_date_obj = datetime.datetime.fromisoformat(row['eventDate'])
            except ValueError as e:
                print(f"Error converting eventDate '{row['eventDate']}' to datetime object: {e}")
                event_date_obj = None
        else:
            event_date_obj = None

       
        if not pd.isnull(row['dateIdentified']):

            try:
                date_identified_obj = pd.to_datetime(row['dateIdentified'])
            except ValueError as e:
                print(f"Error converting dateIdentified '{row['dateIdentified']}' to datetime object: {e}")
                date_identified_obj = None
        else:
            date_identified_obj = None
          

        e = especimen(
            NumeroCatalogo=row['catalogNumber'],
            NombreDelConjuntoDatos=row['datasetName'],
            ComentarioRegistroBiologico=row['occurrenceRemarks'],
            RegistradoPor=row['recordedBy'],
            NumeroIndividuo=row['individualCount'],
            FechaEvento=event_date_obj, # Use the converted eventDate datetime object
            Habitad=row['habitat'],
            Departamento=row['stateProvince'],
            Municipio=row['county'],
            IdentificadoPor=row['identifiedBy'],
            FechaIdentificacion=date_identified_obj, # Use the converted dateIdentified datetime object
            IdentificacionReferencias=row['identificationReferences'],
            ComentarioIdentificacion=row['identificationRemarks'],
            NombreCientificoComentarioRegistroBiologico=row['scientificName'],
            ClaseE=row['class'],
            Orden=row['order'],
            Genero=row['genus'],
            Familia=row['family'],
            NombreComun=row['vernacularName']
        )
        e.save()
    root.mainloop()
    return render(request, 'dashboard.html')

def load_data_clase(request):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1],usecols=[ 'class' ])
  
    for _, row in data.iterrows():
          
        clase = Clase.objects.filter(nombreClase=row['class']).first()
        if not clase:
                clase = Clase(nombreClase=row['class'])
                clase.save()
    root.mainloop()
    return render(request, 'dashboard.html')
def load_data_familia(request):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    
    data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1],usecols=[ 'family' ])
  
    for _, row in data.iterrows():
        familias = familia.objects.filter(nombreFamilia=row['family']).first()
        if not familias:
            familias = familia(nombreFamilia=row['family'])
            familias.save()
    root.mainloop()
    return render(request, 'dashboard.html')
def load_data_orden(request):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    
    data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1],usecols=[ 'order'])
    for _, row in data.iterrows():
        orden = Orden.objects.filter(nombreOrden=row['order']).first()
        if not orden:
            orden = Orden(nombreOrden=row['order'])
            orden.save()

    root.mainloop()
    return render(request, 'dashboard.html')
def load_data_genero(request):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    
    data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1],usecols=[ 'genus'])
  
    for _, row in data.iterrows():
        genero = Genero.objects.filter(nombreGenero=row['genus']).first()
        if not genero:
            genero = Genero(nombreGenero=row['genus'])
            genero.save()
    root.mainloop()
    return render(request, 'dashboard.html')





def element_detail(request, pk):
    element = get_object_or_404(especimen, pk=pk)
    familias =  familia.objects.all()
    ordenes =  Orden.objects.all()
    clases =  Clase.objects.all()
    generos =  Genero.objects.all()
    context = {'element': element,'familias':familias,'ordenes':ordenes,'clases':clases,'generos':generos}
    return render(request, 'paginaejemplar.html', context)


def aprobar_actividad(request, id):
     actividad = UserAction.objects.get(id_user_action = id)
     actividad.estado = True
     actividad.save()
     return HttpResponseRedirect(reverse('dashboardCur')) 

def darbaja_especimen(request, id):
     esp = especimen.objects.get(id=id)
     esp.estado = False
     esp.save()
     return HttpResponseRedirect(reverse('dashboard')) 
