from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from  users.forms import loginForm
from django.urls import reverse
from .models import User, Actividades, TipoActividad,Clase,especimen,UserAction, departamento, municipio,familia,Genero,Orden, Area_User, Class_User , Text
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
from django.http import HttpResponse
from django.db.models import Max
from .models import Text
from django.urls import reverse_lazy
from django.contrib.auth.decorators import  user_passes_test

class IndexView(View):
        def get(self,request):
            text = Text.objects.first
            user = request.user 
            rol =0
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            contex ={'text': text,'rol': rol }
            return render(request,"index.html",contex)
            
class Quienessomos(View):
        def get(self,request):
            rol =0
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"quienessomos.html",{'rol': rol })
class Not_Logged(View):
        def get(self,request):
            return render(request,"notloged.html")            
class CambioContrasenia(View):
        def get(self,request):
            return render(request,"changepassword.html")
class Galry(View):
        def get(self,request):
            rol =0
            anfibios = especimen.objects.filter(NombreDelConjuntoDatos='Colección de Exhibición de Anfibios')
            aves = especimen.objects.filter(NombreDelConjuntoDatos='Colección de Exhibición de Aves')
            reptiles = especimen.objects.filter(NombreDelConjuntoDatos='Colección de exhibición de Reptiles')
            mamiferos = especimen.objects.filter(NombreDelConjuntoDatos='Colección de exhibición de Mammalia')
            especimenes = especimen.objects.all()
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
                
            return render(request,"galery.html",{'especimenes':especimenes,'rol': rol ,'familias':familias,'ordenes':ordenes,'clases':clases,'generos':generos,'anfibios':anfibios,'aves':aves,'mamiferos':mamiferos,'reptiles':reptiles})
def galery_familia(request,nombre):
            rol =0
            especimenes = especimen.objects.filter(Familia = nombre)
            familias =  familia.objects.filter(nombreFamilia = nombre)
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"galery_filter.html",{'especimenes':especimenes,'rol': rol,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_genero(request,nombre):
            rol =0
            especimenes = especimen.objects.filter(Genero = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.all()
            generos =  Genero.objects.filter(nombreGenero = nombre)
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"galery_filter.html",{'especimenes':especimenes,'rol': rol,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_clase(request,nombre):
            rol =0
            especimenes = especimen.objects.filter(ClaseE = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.all()
            clases =  Clase.objects.filter(nombreClase = nombre)
            generos =  Genero.objects.all()
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"galery_filter.html",{'especimenes':especimenes,'rol': rol,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

def galery_orden(request,nombre):
            rol =0
            especimenes = especimen.objects.filter(Orden = nombre)
            familias =  familia.objects.all()
            ordenes =  Orden.objects.filter(nombreOrden = nombre)
            clases =  Clase.objects.all()
            generos =  Genero.objects.all()
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"galery_filter.html",{'especimenes':especimenes,'rol': rol,'ordenes':ordenes,'clases':clases,'generos':generos,'familias':familias})

class Dashboard_Aux(View):
        
        @method_decorator(login_required(login_url='redirect')   ) 
        def get(self,request):

            user = request.user 
            if user.is_authenticated:
                if Rol.objects.filter(user=user, id=1):
  

                    clase = Class_User.objects.get(id_user_id= request.user.id)
                    c = Clase.objects.get(id = clase.id_clase_id)
                    actions = UserAction.objects.filter(user=request.user).order_by('tiempo')
                    especimenes = especimen.objects.filter(ClaseE = c.nombreClase)
                    return render(request,"dashauxiliar.html",{'especimenes':especimenes,'actions':actions})
                else:
                      return HttpResponseRedirect(reverse('redirect'))

            else:
          
                return HttpResponseRedirect(reverse('redirect'))
class Dashboard_Pas(View):
        @method_decorator(login_required(login_url='redirect')   ) 
        def get(self,request):
            user = request.user 
            if user.is_authenticated:
                if Rol.objects.filter(user=user, id=2):
  
                    return render(request,"dashpasante.html")
                else:
                    return HttpResponseRedirect(reverse('redirect'))

            else:
        
                return HttpResponseRedirect(reverse('redirect'))
class Dashboard_Cur(View):
        def get(self,request):
            user = request.user 
            if user.is_authenticated:
                if Rol.objects.filter(user=user, id=3):
                    clase = Class_User.objects.get(id_user_id= request.user.id)
                    #Filtrar por usuarios del area
                    usuarios = Class_User.objects.filter(id_clase_id = clase.id_clase_id)
                    lista = []
                    for i in usuarios:
                        lista.append(i.id_user_id)
                    c = Clase.objects.get(id = clase.id_clase_id)
                    print(c.nombreClase)
                    especimenes = especimen.objects.filter(ClaseE = c.nombreClase)
                    actions = UserAction.objects.filter(user__in = lista)
                    return render(request,"dashcurador.html",{'actions': actions, 'especimenes':especimenes})
                else:
                    return HttpResponseRedirect(reverse('redirect'))

            else:
        
                return HttpResponseRedirect(reverse('redirect'))
class Dashboard(View):
        
        def get(self,request):
            
            user = request.user 
            if user.is_authenticated:
                
                if Rol.objects.filter(user=user, id=4):
                  
                    especimenes = especimen.objects.all()
                    actions = UserAction.objects.order_by('tiempo').all()
                    return render(request,"dashboard.html",{'especimenes':especimenes,'actions': actions})
                else:
                    return HttpResponseRedirect(reverse('redirect'))

            else:
        
                return HttpResponseRedirect(reverse('redirect'))
class PerfilU(View):
        def get(self,request):

            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"profile.html",{'rol': rol })		            		
class EjemplarP(View):
        def get(self,request):
            rol =0
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
            return render(request,"paginaejemplar.html",{'rol': rol })		            		


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
    user1 = request.user 
    if user1.is_authenticated:
            rol = Rol.objects.get(user=user1)
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
            clase = form.cleaned_data['area']
            area_clase = Class_User(id_user = User.objects.get(id=user.id), id_clase = Clase.objects.get(id=clase))
            area_clase.save()
            
    else:
        form = CustomUser()
    return render(request, 'registerUser.html', {'form':form,'rol': rol })

@login_required(login_url='redirect')
def registroActividad(request):
    user = request.user 
    if user.is_authenticated:
           rol = Rol.objects.get(user=user)
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
    return render(request, 'informe1.html', {'form':form,'rol': rol})


@login_required(login_url='redirect')
def registerE(request):
    user = request.user 
    if user.is_authenticated:
           rol = Rol.objects.get(user=user)
    if request.method == 'POST':
        form = EjemplarForm(request.POST)
        
        if form.is_valid():
            print('emtre')
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
            #Imagen = form.changed_data['Image']

            e = especimen(NumeroCatalogo=NumeroCatalogo,NombreDelConjuntoDatos= NombreDelConjuntoDatos, ComentarioRegistroBiologico = ComentarioRegistroBiologico 
            , RegistradoPor = RegistradoPor,NumeroIndividuo=NumeroIndividuo,FechaEvento=FechaEvento,Habitad=Habitad,Departamento=departamento.objects.get(id=Departamento),Municipio=municipio.objects.get(id=Municipio)
            ,IdentificadoPor=IdentificadoPor,FechaIdentificacion=FechaIdentificacion,IdentificacionReferencias=IdentificacionReferencias,ComentarioIdentificacion=ComentarioIdentificacion,
            NombreCientificoComentarioRegistroBiologico=NombreCientificoComentarioRegistroBiologico,ClaseE=Clase,Orden = Orden, Genero = Genero
            ,Familia = Familia, NombreComun=NombreComun, Image = "")
            e.Image = request.FILES.get('imagen')
            print(e.Image)
            e.save()

            NumeroCatalogo = e.NumeroCatalogo
            TareaRealizada = 4
            Hora = datetime.now().time()
            Fecha = datetime.now().date()
            Descripcion = 'Se agrego el ejemplar ' + NumeroCatalogo
            a = Actividades(NumeroCatalogo=NumeroCatalogo,TareaRealizada= TipoActividad.objects.get(id=TareaRealizada), Hora = Hora , Fecha = Fecha,Descripcion=Descripcion)   
            a.save()
            userAction = UserAction(user=request.user, tarea= TipoActividad.objects.get(id=TareaRealizada),ejemplar= NumeroCatalogo)
            userAction.save()
    else:
        form = EjemplarForm()
    return render(request, 'registerE.html', {'form':form,'rol': rol}) 
   
@login_required(login_url='redirect')
def custom_logout(request):
    logout(request)
    
    return redirect("home")

class update_ejemplar(View):
        
        def get(self,request,id):
            rol =0
            user = request.user 
            if user.is_authenticated:
                rol = Rol.objects.get(user=user)
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
            
            return render(request,"updateE.html",{'contexto':contexto,'rol': rol})

def update_record_ejemplar(request,id):
    user = request.user 
    if user.is_authenticated:
           rol = Rol.objects.get(user=user)
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
    return render(request, 'UpdateUser.html', {'form':form ,'rol': rol})
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
    return render(request, 'UpdateUser.html', {'form':form ,'rol': rol})    
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
    return render(request, 'UpdateUser.html', {'form':form ,'rol': rol})    
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
    return render(request, 'UpdateUser.html', {'form':form ,'rol': rol})    
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
def elegir(request):
    if request.method == 'POST':
        if request.POST.get('option') == 'option1':
           
            return load_data_clase(request)
        elif request.POST.get('option') == 'option2':
         
            return load_data_orden(request)
        elif request.POST.get('option') == 'option3':
            return load_data_familia(request)
        elif request.POST.get('option') == 'option4':
            return load_data_genero(request)
        else:
            return HttpResponse('Invalid option')
    else:
        return redirect('dashboard.html')
def load_data_clase(request):
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
        if not file_path: 
            messages.error(request, 'Error: No se seleccionó un archivo')
            return redirect('dashboard')
        
        data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1], usecols=['class'])
        for _, row in data.iterrows():
            clase = Clase.objects.filter(nombreClase=row['class']).first()
            if not clase:
                clase = Clase(nombreClase=row['class'])
                clase.save()
        root.mainloop()
        return render(request, 'dashboard.html')
    except FileNotFoundError:
        return redirect('dashboard')
    
def load_data_familia(request):
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
        if not file_path: 
            messages.error(request, 'Error: No se seleccionó un archivo')
            return redirect('dashboard')
        
        data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1], usecols=['family'])
        for _, row in data.iterrows():
            fam = familia.objects.filter(nombreFamilia=row['family']).first()
            if not fam:
                fam = familia(nombreFamilia=row['family'])
                fam.save()
        root.mainloop()
        return render(request, 'dashboard.html')
    except FileNotFoundError:
        return redirect('dashboard')
   




def load_data_orden(request):
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
        if not file_path: 
            messages.error(request, 'Error: No se seleccionó un archivo')
            return redirect('dashboard')
        
        data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1], usecols=['order'])
        for _, row in data.iterrows():
            orden = Orden.objects.filter(nombreOrden=row['order']).first()
            if not orden:
                orden = Orden(nombreOrden=row['order'])
                orden.save()
        root.mainloop()
        return render(request, 'dashboard.html')
    except FileNotFoundError:
        return redirect('dashboard')
def load_data_genero(request):
    try:
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(parent=root,title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
        if not file_path: 
            messages.error(request, 'Error: No se seleccionó un archivo')
            return redirect('dashboard')
        
        data = pd.read_excel(file_path, sheet_name="Plantilla", skiprows=[1], usecols=['genus'])
        for _, row in data.iterrows():
            genero = Genero.objects.filter(nombreGenero=row['genus']).first()
            if not genero:
                genero = Genero(nombreGenero=row['genus'])
                genero.save()
        root.mainloop()
        return render(request, 'dashboard.html')
    except FileNotFoundError:
        return redirect('dashboard')



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
     if actividad.tarea == 'Archivar un ejemplar':
          print("Entre")
          print(actividad.ejemplar)
          ejemplar = especimen.objects.get(NumeroCatalogo=actividad.ejemplar)
          ejemplar.estado = False
          ejemplar.save()
          actividad.estado = True
          actividad.save()
     else:
          actividad.estado = True
          actividad.save()
     return HttpResponseRedirect(reverse('dashboardCur')) 

def darbaja_especimen(request, id):
    esp = especimen.objects.get(id=id)
    if request.user.groups.filter(name__in=['Auxiliar']):
            NumeroCatalogo = esp.NumeroCatalogo
            TareaRealizada = 8
            Hora = datetime.now().time()
            Fecha = datetime.now().date()
            Descripcion = 'Se Archivo el ejemplar ' + NumeroCatalogo
            a = Actividades(NumeroCatalogo=NumeroCatalogo,TareaRealizada= TipoActividad.objects.get(id=TareaRealizada), Hora = Hora , Fecha = Fecha,Descripcion=Descripcion)   
            a.save()
            userAction = UserAction(user=request.user, tarea= TipoActividad.objects.get(id=TareaRealizada),ejemplar= NumeroCatalogo)
            userAction.save()
            return HttpResponseRedirect(reverse('dashboardAux'))
    if request.user.groups.filter(name__in=['Pasante']):
        esp = especimen.objects.get(id=id)
        esp.estado = False
        esp.save()                   
        return HttpResponseRedirect(reverse('dashboardPas'))
    if request.user.groups.filter(name__in=['Curador']):
        esp = especimen.objects.get(id=id)
        esp.estado = False
        esp.save()            
        return HttpResponseRedirect(reverse('dashboardCur'))
    esp = especimen.objects.get(id=id)
    esp.estado = False
    esp.save()
    return HttpResponseRedirect(reverse('dashboard')) 
def AgregarActividad(request):
    if request.method == 'POST':
        form = TipoActividadForm(request.POST)
        nombreactividad =  request.POST.get('name')
        max_id = TipoActividad.objects.all().aggregate(Max('id'))['id__max']
        a = TipoActividad(id=max_id + 1, nombreactividad=nombreactividad) 
        a.save()
        return redirect('dashboard') 
    else:
        form = TipoActividadForm()
    return render(request, 'dashboard.html', {'form': form})
def estado_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'desactivarUsuario.html', {'usuarios': usuarios})


def desactivar_usuario(request,id):
     usuario = User.objects.get(id=id)
     print(usuario.id)
     usuario.is_active = False
     usuario.save()
     return HttpResponseRedirect(reverse('dashboard')) 
        

def update_text(request):
    if request.method == 'POST':
        text =Text.objects.get(pk=2)
        text.content = request.POST['texto'] 
        text.save() 
        return redirect('dashboard') 
    else:
        return render(request, 'dashboard.html')


   
def elegir_texto(request):
    if request.method == 'POST':
        if request.POST.get('optiontexto') == 'option1':
            text =Text.objects.get(pk=2)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 

        elif request.POST.get('optiontexto') == 'option2':
            text =Text.objects.get(pk=3)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 
       
        elif request.POST.get('optiontexto') == 'option3':
            text =Text.objects.get(pk=4)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 
        elif request.POST.get('optiontexto') == 'option4':
            text =Text.objects.get(pk=5)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard')
        elif request.POST.get('optiontexto') == 'option5':
            text =Text.objects.get(pk=6)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 
        elif request.POST.get('optiontexto') == 'option6':
            text =Text.objects.get(pk=7)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 
        elif request.POST.get('optiontexto') == 'option7':
            text =Text.objects.get(pk=8)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard') 
        elif request.POST.get('optiontexto') == 'option8':
            text =Text.objects.get(pk=9)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard')  
        elif request.POST.get('optiontexto') == 'option9':
            text =Text.objects.get(pk=10)
            text.content = request.POST['texto'] 
            text.save() 
            return redirect('dashboard')
       
        else:
            return HttpResponse('Invalid option')
    else:
        return redirect('dashboard.html')    