from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from users.forms import *
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.urls import reverse
from .models import *
from .forms import loginForm
from django.shortcuts import render, redirect
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
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Max
from .models import Text
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
import qrcode
import io
from io import BytesIO
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.views.generic.edit import FormView
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.core.mail import send_mail
from django.http import JsonResponse
class IndexView(View):
    def get(self, request):
        texto = {
            "text1": Text.objects.get(id=2),
            "text2": Text.objects.get(id=3),
            "text3": Text.objects.get(id=4),
            "text4": Text.objects.get(id=5),
            "text5": Text.objects.get(id=6),
            "text6": Text.objects.get(id=7),
            "text7": Text.objects.get(id=8),
            "text8": Text.objects.get(id=9),
            "text9": Text.objects.get(id=10),
        }
        user = request.user
        rol = 0
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        contex = {"text": texto, "rol": rol}
        return render(request, "index.html", contex)


class Quienessomos(View):
    def get(self, request):
        rol = 0
        user = request.user
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        return render(request, "quienessomos.html", {"rol": rol})


class Not_Logged(View):
    def get(self, request):
        return render(request, "notloged.html")
def exito(request):
    rol = 0
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    return render(request, "exito.html",{"rol": rol})

class CambioContrasenia(View):
    def get(self, request):
        return render(request, "changepassword.html")


class Galry(View):
    def get(self, request):
        rol = 0
        anfibios = especimen.objects.filter(
            NombreDelConjuntoDatos="Colección de Exhibición de Anfibios"
        )
        aves = especimen.objects.filter(
            NombreDelConjuntoDatos="Colección de Exhibición de Aves"
        )
        reptiles = especimen.objects.filter(
            NombreDelConjuntoDatos="Colección de exhibición de Reptiles"
        )
        mamiferos = especimen.objects.filter(
            NombreDelConjuntoDatos="Colección de exhibición de Mammalia"
        )
        especimenes = especimen.objects.all()
        familias = familia.objects.all()
        ordenes = Orden.objects.all()
        clases = Clase.objects.all()
        generos = Genero.objects.all()
        user = request.user
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        return render(
            request,
            "galery.html",
            {
                "especimenes": especimenes,
                "rol": rol,
                "familias": familias,
                "ordenes": ordenes,
                "clases": clases,
                "generos": generos,
                "anfibios": anfibios,
                "aves": aves,
                "mamiferos": mamiferos,
                "reptiles": reptiles,
            },
        )


def galery_familia(request, nombre):
    rol = 0
    especimenes = especimen.objects.filter(Familia=nombre)
    familias = familia.objects.filter(nombreFamilia=nombre)
    ordenes = Orden.objects.all()
    clases = Clase.objects.all()
    generos = Genero.objects.all()
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    return render(
        request,
        "galery_filter.html",
        {
            "especimenes": especimenes,
            "rol": rol,
            "ordenes": ordenes,
            "clases": clases,
            "generos": generos,
            "familias": familias,
        },
    )


def galery_genero(request, nombre):
    rol = 0
    especimenes = especimen.objects.filter(Genero=nombre)
    familias = familia.objects.all()
    ordenes = Orden.objects.all()
    clases = Clase.objects.all()
    generos = Genero.objects.filter(nombreGenero=nombre)
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    return render(
        request,
        "galery_filter.html",
        {
            "especimenes": especimenes,
            "rol": rol,
            "ordenes": ordenes,
            "clases": clases,
            "generos": generos,
            "familias": familias,
        },
    )


def galery_clase(request, nombre):
    rol = 0
    especimenes = especimen.objects.filter(ClaseE=nombre)
    familias = familia.objects.all()
    ordenes = Orden.objects.all()
    clases = Clase.objects.filter(nombreClase=nombre)
    generos = Genero.objects.all()
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    return render(
        request,
        "galery_filter.html",
        {
            "especimenes": especimenes,
            "rol": rol,
            "ordenes": ordenes,
            "clases": clases,
            "generos": generos,
            "familias": familias,
        },
    )


def galery_orden(request, nombre):
    rol = 0
    especimenes = especimen.objects.filter(Orden=nombre)
    familias = familia.objects.all()
    ordenes = Orden.objects.filter(nombreOrden=nombre)
    clases = Clase.objects.all()
    generos = Genero.objects.all()
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    return render(
        request,
        "galery_filter.html",
        {
            "especimenes": especimenes,
            "rol": rol,
            "ordenes": ordenes,
            "clases": clases,
            "generos": generos,
            "familias": familias,
        },
    )


class Dashboard_Aux(View):
    @method_decorator(login_required(login_url="redirect"))
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if Rol.objects.filter(user=user, id=1):
                clase = Class_User.objects.get(id_user_id=request.user.id)
                c = Clase.objects.get(id=clase.id_clase_id)
                actions = UserAction.objects.filter(user=request.user).order_by(
                    "tiempo"
                )
                especimenes = especimen.objects.filter(ClaseE=c.nombreClase)
                return render(
                    request,
                    "dashauxiliar.html",
                    {"especimenes": especimenes, "actions": actions},
                )
            else:
                return HttpResponseRedirect(reverse("redirect"))

        else:
            return HttpResponseRedirect(reverse("redirect"))


class Dashboard_Pas(View):
    @method_decorator(login_required(login_url="redirect"))
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if Rol.objects.filter(user=user, id=2):
                return render(request, "dashpasante.html")
            else:
                return HttpResponseRedirect(reverse("redirect"))

        else:
            return HttpResponseRedirect(reverse("redirect"))


class Dashboard_Cur(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if Rol.objects.filter(user=user, id=3):
                clase = Class_User.objects.get(id_user_id=request.user.id)
                usuarios = Class_User.objects.filter(id_clase_id=clase.id_clase_id)
                lista = []
                for i in usuarios:
                    lista.append(i.id_user_id)
                c = Clase.objects.get(id=clase.id_clase_id)
                clase_genero = c.nombreClase
                especimenes = especimen.objects.filter(ClaseE=c.nombreClase)
                actions = UserAction.objects.filter(user__in=lista)
                return render(
                    request,
                    "dashcurador.html",
                    {
                        "actions": actions,
                        "especimenes": especimenes,
                        "clase": clase_genero,
                    },
                )
            else:
                return HttpResponseRedirect(reverse("redirect"))

        else:
            return HttpResponseRedirect(reverse("redirect"))


class Dashboard(View):
    def get(self, request):
        error = request.session.pop("error", None)
        success = request.session.pop("success", None)
        context = {}
        if error:
            context.update({"error": error})
        if success:
            context.update({"success": success})
        user = request.user
        actividades = TipoActividad.objects.all()

        if user.is_authenticated:
            if Rol.objects.filter(user=user, id=4):
                especimenes = especimen.objects.all()
                actions = UserAction.objects.order_by("tiempo").all()
                context.update(
                    {
                        "especimenes": especimenes,
                        "actions": actions,
                        "actividades": actividades,
                    }
                )
                return render(request, "dashboard.html", context)
            else:
                return HttpResponseRedirect(reverse("redirect"))

        else:
            return HttpResponseRedirect(reverse("redirect"))


class PerfilU(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        return render(request, "profile.html", {"rol": rol})


class EjemplarP(View):
    def get(self, request):
        rol = 0
        user = request.user
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        return render(request, "paginaejemplar.html", {"rol": rol})


def obtener_usuario(request, id_usuario):
    User = get_user_model()
    user = User.objects.get(id=id_usuario)
   
    usuario_info = {
        "nombre": user.nombre,
        "apellido": user.apellido,
        "correo": user.email,
    }
    return JsonResponse(usuario_info)


def login(request):
    form = loginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    if user.groups.filter(name__in=["Auxiliar"]):
                        return HttpResponseRedirect(reverse("dashboardAux"))
                    if user.groups.filter(name__in=["Pasante"]):
                        return HttpResponseRedirect(reverse("dashboardPas"))
                    if user.groups.filter(name__in=["Curador"]):
                        return HttpResponseRedirect(reverse("dashboardCur"))
                    return HttpResponseRedirect(reverse("dashboard"))

    return render(request, "login.html", {"form": form})


@login_required(login_url="redirect")
def register(request):
    user1 = request.user
    if user1.is_authenticated:
        rol = Rol.objects.get(user=user1)
    if request.method == "POST":
        form = CustomUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            correo = form.cleaned_data["correo"]
            password = form.cleaned_data["password"]
            rol1 = form.cleaned_data["rol"]
            rolusuario = Rol.objects.get(id=rol1)
            User = get_user_model()
            user = User.objects.create_user(username=username, email=correo, password=password ,rol=rolusuario  )
            user.nombre = nombre
            user.apellido = apellido
           
            user.save()

            user.is_superuser = False
            user.is_staff = False
            user.is_active = True
            user.save()

           
            clase = form.cleaned_data["area"]
            area_clase = Class_User(
                id_user=User.objects.get(id=user.id),
                id_clase=Clase.objects.get(id=clase),
            )
            area_clase.save()
            return redirect("dashboard")
    else:
        form = CustomUser()
    return render(request, "registerUser.html", {"form": form, "rol": rol})


@login_required(login_url="redirect")
def registroActividad(request):
    a = request.user.rol
    user1 = request.user
    if user1.is_authenticated:
        rol = Rol.objects.get(user=user1)
    if a.id == 4:
        especimenes = especimen.objects.all()
    else:
        clase = Class_User.objects.get(id_user_id=request.user.id)
        clas = Clase.objects.get(id=clase.id_clase_id)
        especimenes = especimen.objects.filter(ClaseE=clas.nombreClase)
    form = ActividadesForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            NumeroCatalogo = request.POST["NumeroCatalogo"]
            TareaRealizada = form.cleaned_data["TareaRealizada"]
            Hora = form.cleaned_data["Hora"]
            Fecha = form.cleaned_data["Fecha"]
            Descripcion = form.cleaned_data["Descripcion"]
          
            a = Actividades(
                NumeroCatalogo=especimen.objects.get(id=NumeroCatalogo),
                TareaRealizada=TipoActividad.objects.get(id=TareaRealizada),
                Hora=Hora,
                Fecha=Fecha,
                Descripcion=Descripcion,
            )
            a.save()
            rol_id = request.user.rol.id
            if rol_id == 4 or rol_id == 3:
                estado = True
            else:
                estado = False

            userAction = UserAction(
                user=request.user,
                tarea=TipoActividad.objects.get(id=TareaRealizada),
                ejemplar=especimen.objects.get(id=NumeroCatalogo),
                estado=estado,
                Descripcion=Descripcion,
            )
            userAction.save()

            rol_id = request.user.rol.id

            if rol_id == 4:
                return redirect("dashboard")
            elif rol_id == 1:
                return redirect("dashboardAux")
            elif rol_id == 2:
                return redirect("dashboardPas")
            elif rol_id == 3:
                return redirect("dashboardCur")
    else:
        form = ActividadesForm()
    return render(
        request, "informe1.html", {"form": form, "especimenes": especimenes, "rol": rol}
    )


@login_required(login_url="redirect")
def registerE(request):
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    if request.method == "POST":
        form = EjemplarForm(request.POST, files=request.FILES)

        if form.is_valid():
            print("emtre")
            NumeroCatalogo = form.cleaned_data["NumeroCatalogo"]
            NombreDelConjuntoDatos = form.cleaned_data["NombreDelConjuntoDatos"]
            ComentarioRegistroBiologico = form.cleaned_data[
                "ComentarioRegistroBiologico"
            ]
            RegistradoPor = form.cleaned_data["RegistradoPor"]
            NumeroIndividuo = form.cleaned_data["NumeroIndividuo"]
            FechaEvento = form.cleaned_data["FechaEvento"]
            Habitad = form.cleaned_data["Habitad"]
            Departamento = form.cleaned_data["Departamento"]
            Municipio = form.cleaned_data["Municipio"]
            IdentificadoPor = form.cleaned_data["IdentificadoPor"]
            FechaEvento = form.cleaned_data["FechaEvento"]
            FechaIdentificacion = form.cleaned_data["FechaIdentificacion"]
            IdentificacionReferencias = form.cleaned_data["FechaEvento"]
            ComentarioIdentificacion = form.cleaned_data["ComentarioIdentificacion"]
            NombreCientificoComentarioRegistroBiologico = form.cleaned_data[
                "NombreCientificoComentarioRegistroBiologico"
            ]
            ClaseE = form.cleaned_data["ClaseE"]
            orden = form.cleaned_data["Orden"]
            genero = form.cleaned_data["Genero"]
            ffamilia = form.cleaned_data["Familia"]
            NombreComun = form.cleaned_data["NombreComun"]
            nombreclase = Clase.objects.get(id=ClaseE)
            nombreorder = Orden.objects.get(id=orden)
            nombregenero = Genero.objects.get(id=genero)
            nombrefamilia = familia.objects.get(id=ffamilia)
            e = especimen(
                NumeroCatalogo=NumeroCatalogo,
                NombreDelConjuntoDatos=NombreDelConjuntoDatos,
                ComentarioRegistroBiologico=ComentarioRegistroBiologico,
                RegistradoPor=RegistradoPor,
                NumeroIndividuo=NumeroIndividuo,
                FechaEvento=FechaEvento,
                Habitad=Habitad,
                Departamento=departamento.objects.get(id=Departamento),
                Municipio=municipio.objects.get(id=Municipio),
                IdentificadoPor=IdentificadoPor,
                FechaIdentificacion=FechaIdentificacion,
                IdentificacionReferencias=IdentificacionReferencias,
                ComentarioIdentificacion=ComentarioIdentificacion,
                NombreCientificoComentarioRegistroBiologico=NombreCientificoComentarioRegistroBiologico,
                ClaseE=nombreclase.nombreClase,
                Orden=nombreorder.nombreOrden,
                Genero=nombregenero.nombreGenero,
                Familia=nombrefamilia.nombreFamilia,
                NombreComun=NombreComun,
            )
            e.Image = request.FILES.get("imagen")
            print(e.Image)

            e.save()
            print(nombreclase.nombreClase)
            NumeroCatalogo = e.NumeroCatalogo
            TareaRealizada = 4
            Hora = datetime.now().time()
            Fecha = datetime.now().date()
            Descripcion = "Se agrego el ejemplar " + NumeroCatalogo
            a = Actividades(
                NumeroCatalogo=NumeroCatalogo,
                TareaRealizada=TipoActividad.objects.get(id=TareaRealizada),
                Hora=Hora,
                Fecha=Fecha,
                Descripcion=Descripcion,
            )
            a.save()
            userAction = UserAction(
                user=request.user,
                tarea=TipoActividad.objects.get(id=TareaRealizada),
                ejemplar=NumeroCatalogo,
            )
            userAction.save()

            rol_id = request.user.rol.id

            if rol_id == 4:
                return redirect("dashboard")
            elif rol_id == 1:
                return redirect("dashboardAux")
            elif rol_id == 2:
                return redirect("dashboardPas")
            elif rol_id == 3:
                return redirect("dashboardCur")

    else:
        form = EjemplarForm()
    return render(request, "registerE.html", {"form": form, "rol": rol})


@login_required(login_url="redirect")
def custom_logout(request):
    logout(request)

    return redirect("home")


class update_ejemplar(View):
    def get(self, request, id):
        rol = 0
        user = request.user
        if user.is_authenticated:
            rol = Rol.objects.get(user=user)
        ejemplar = especimen.objects.get(pk=id)
        contexto = {
            "id": ejemplar.id,
            "numeroCatalogo": ejemplar.NumeroCatalogo,
            "nombreDelConjuntoDatos": ejemplar.NombreDelConjuntoDatos,
            "comentarioRegistro": ejemplar.ComentarioRegistroBiologico,
            "registrado": ejemplar.RegistradoPor,
            "numeroIndividuo": ejemplar.NumeroIndividuo,
            "fechaEvento": ejemplar.FechaEvento,
            "habitad": ejemplar.Habitad,
            "departamento": ejemplar.Departamento,
            "municipio": ejemplar.Municipio,
            "identificadoPor": ejemplar.IdentificadoPor,
            "fechaIdentificacion": ejemplar.FechaIdentificacion,
            "identificacionReferencias": ejemplar.IdentificacionReferencias,
            "comentarioIdentificacion": ejemplar.ComentarioIdentificacion,
            "nombreCientifico": ejemplar.NombreCientificoComentarioRegistroBiologico,
            "clase": ejemplar.ClaseE,
            "orden": ejemplar.Orden,
            "genero": ejemplar.Genero,
            "familia": ejemplar.Familia,
            "image": ejemplar.Image,
            "nombreComun": ejemplar.NombreComun,
        }

        return render(request, "updateE.html", {"contexto": contexto, "rol": rol})


def update_record_ejemplar(request, id):
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    numero = request.POST["NumeroCatalogo"]
    nombredeDatos = request.POST["NombreDelConjuntoDatos"]
    comentarioRegistro = request.POST["ComentarioRegistroBiologico"]
    registradoPor = request.POST["RegistradoPor"]
    numeroIndividuo = request.POST["NumeroIndividuo"]

    habitad = request.POST["Habitad"]
    departamento = request.POST["Departamento"]
    municipio = request.POST["Municipio"]
    identificadoPor = request.POST["IdentificadoPor"]
    idetificacionReferencias = request.POST["IdentificacionReferencias"]
    comentarioIdentificacion = request.POST["ComentarioIdentificacion"]
    nombreCientifico = request.POST["NombreCientifico"]
    clase = request.POST["Clase"]
    orden = request.POST["Orden"]
    genero = request.POST["Genero"]
    familia = request.POST["Familia"]
    nombreComun = request.POST["NombreComun"]
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
    ejemplar.Orden = orden
    ejemplar.Genero = genero
    ejemplar.Familia = familia
    ejemplar.NombreComun = nombreComun
    ejemplar.Image = request.FILES.get("imagen")

    ejemplar.save()

    NumeroCatalogo = ejemplar.NumeroCatalogo
    TareaRealizada = 4
    Hora = datetime.now().time()
    Fecha = datetime.now().date()
    Descripcion = "Se actualizo información de  " + NumeroCatalogo
    a = Actividades(
        NumeroCatalogo=NumeroCatalogo,
        TareaRealizada=TipoActividad.objects.get(id=TareaRealizada),
        Hora=Hora,
        Fecha=Fecha,
        Descripcion=Descripcion,
    )
    a.save()
    userAction = UserAction(
        user=request.user,
        tarea=TipoActividad.objects.get(id=TareaRealizada),
        ejemplar=NumeroCatalogo,
    )
    userAction.save()
    if request.user.groups.filter(name__in=["Auxiliar"]):
        return HttpResponseRedirect(reverse("dashboardAux"))
    if request.user.groups.filter(name__in=["Pasante"]):
        return HttpResponseRedirect(reverse("dashboardPas"))
    if request.user.groups.filter(name__in=["Curador"]):
        return HttpResponseRedirect(reverse("dashboardCur"))
    return HttpResponseRedirect(reverse("dashboard"))


@login_required(login_url="redirect")
def update_aux_curatoria(request):
    rol = 0
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    if request.method == "POST":
        form = Update(request.POST)
        if form.is_valid():
            User = get_user_model()
            username = form.cleaned_data["username"]
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            correo = form.cleaned_data["correo"]
            rol = form.cleaned_data["rol"]
            user = User.objects.get(id=username)
            user.nombre = nombre
            user.apellido = apellido
            user.email = correo
            user.rol = Rol.objects.get(id=rol)
            user.save()

            rol_id = request.user.rol.id

            if rol_id == 4:
                return redirect("dashboard")
            elif rol_id == 1:
                return redirect("dashboardAux")
            elif rol_id == 2:
                return redirect("dashboardPas")
            elif rol_id == 3:
                return redirect("dashboardCur")
    else:
        username = request.GET.get('username')
        if username:
            user = User.objects.get(username=username)
            form = Update(initial={
                'username': user.username,
                'nombre': user.nombre,
                'apellido': user.apellido,
                'correo': user.email,
                'rol': user.rol.id,
            })
        else:
            form = Update()
    return render(request, "UpdateUser.html", {"form": form, "rol": rol})



def load_data(request):
    if request.method == "POST" and request.FILES.get("excel_file_especimenes"):
        excel_file = request.FILES["excel_file_especimenes"]
        try:
            data = pd.read_excel(
                excel_file,
                sheet_name="Plantilla",
                skiprows=[1],
                usecols=[
                    "catalogNumber",
                    "datasetName",
                    "occurrenceRemarks",
                    "recordedBy",
                    "individualCount",
                    "eventDate",
                    "habitat",
                    "stateProvince",
                    "county",
                    "identifiedBy",
                    "dateIdentified",
                    "identificationReferences",
                    "identificationRemarks",
                    "scientificName",
                    "class",
                    "order",
                    "family",
                    "genus",
                    "vernacularName",
                ],
            )

            for _, row in data.iterrows():
                catalog_number = row["catalogNumber"]
                if especimen.objects.filter(Q(NumeroCatalogo=catalog_number)).exists():
                    continue

                for col in [
                    "datasetName",
                    "occurrenceRemarks",
                    "recordedBy",
                    "individualCount",
                    "eventDate",
                    "habitat",
                    "stateProvince",
                    "county",
                    "identifiedBy",
                    "dateIdentified",
                    "identificationReferences",
                    "identificationRemarks",
                    "scientificName",
                    "class",
                    "order",
                    "family",
                    "genus",
                    "vernacularName",
                ]:
                    if pd.isnull(row[col]):
                        row[col] = None

                if not pd.isnull(row["eventDate"]):
                    try:
                        event_date_obj = pd.to_datetime(row["eventDate"])
                    except ValueError as e:
                        print(f"Error converting eventDate '{row['eventDate']}' to datetime object: {e}")
                        event_date_obj = None
                else:
                    event_date_obj = None

                if not pd.isnull(row["dateIdentified"]):
                    try:
                        date_identified_obj = pd.to_datetime(row["dateIdentified"])
                    except ValueError as e:
                        print(f"Error converting dateIdentified '{row['dateIdentified']}' to datetime object: {e}")
                        date_identified_obj = None
                else:
                    date_identified_obj = None

                e = especimen(
                    NumeroCatalogo=catalog_number,
                    NombreDelConjuntoDatos=row["datasetName"],
                    ComentarioRegistroBiologico=row["occurrenceRemarks"],
                    RegistradoPor=row["recordedBy"],
                    NumeroIndividuo=row["individualCount"],
                    FechaEvento=event_date_obj,
                    Habitad=row["habitat"],
                    Departamento=row["stateProvince"],
                    Municipio=row["county"],
                    IdentificadoPor=row["identifiedBy"],
                    FechaIdentificacion=date_identified_obj,
                    IdentificacionReferencias=row["identificationReferences"],
                    ComentarioIdentificacion=row["identificationRemarks"],
                    NombreCientificoComentarioRegistroBiologico=row["scientificName"],
                    ClaseE=row["class"],
                    Orden=row["order"],
                    Genero=row["genus"],
                    Familia=row["family"],
                    NombreComun=row["vernacularName"],
                )
                e.save()

            return render(request, "exito.html")

        except Exception as e:
           print(f"Error occurred while loading data from file: {e}")

        
    return render(request, "exito.html")



def elegir(request):
    if request.method == "POST":
        if request.POST.get("option") == "option1":
            return load_data_clase(request)
        elif request.POST.get("option") == "option2":
            return load_data_orden(request)
        elif request.POST.get("option") == "option3":
            return load_data_familia(request)
        elif request.POST.get("option") == "option4":
            return load_data_genero(request)
        else:
            return HttpResponse("Invalid option")
    else:
        return redirect("dashboard.html")


def load_data_clase(request):
    if request.method == "POST" and request.FILES.get("excel_file_clase"):
        excel_file = request.FILES["excel_file_clase"]

        try:
            data = pd.read_excel(
                excel_file,
                sheet_name="Plantilla",
                skiprows=[1],
                usecols=["class"]
            )

            for _, row in data.iterrows():
                clase = Clase.objects.filter(nombreClase=row["class"]).first()
                if not clase:
                    clase = Clase(nombreClase=row["class"])
                    clase.save()

            messages.success(request, "Los datos se cargaron exitosamente")
        except Exception as e:
            messages.error(request, f"Error al cargar el archivo: {str(e)}")

    return redirect("dashboard")


def load_data_familia(request):
    if request.method == "POST" and request.FILES.get("excel_file_familia"):
        excel_file = request.FILES["excel_file_familia"]

        try:
            data = pd.read_excel(
                excel_file,
                sheet_name="Plantilla",
                skiprows=[1],
                usecols=["family"]
            )

            for _, row in data.iterrows():
                fam = familia.objects.filter(nombreFamilia=row["family"]).first()
                if not fam:
                    fam = familia(nombreFamilia=row["family"])
                    fam.save()

            messages.success(request, "Los datos se cargaron exitosamente")
        except Exception as e:
            messages.error(request, f"Error al cargar el archivo: {str(e)}")

    return redirect("dashboard")

def load_data_orden(request):
    if request.method == "POST" and request.FILES.get("excel_file_orden"):
        excel_file = request.FILES["excel_file_orden"]

        try:
            data = pd.read_excel(
                excel_file,
                sheet_name="Plantilla",
                skiprows=[1],
                usecols=["order"]
            )

            for _, row in data.iterrows():
                orden = Orden.objects.filter(nombreOrden=row["order"]).first()
                if not orden:
                    orden = Orden(nombreOrden=row["order"])
                    orden.save()

            messages.success(request, "Los datos se cargaron exitosamente")
        except Exception as e:
            messages.error(request, f"Error al cargar el archivo: {str(e)}")

    return redirect("dashboard")


def load_data_genero(request):
    if request.method == "POST" and request.FILES.get("excel_file_genero"):
        excel_file = request.FILES["excel_file_genero"]

        try:
            data = pd.read_excel(
                excel_file,
                sheet_name="Plantilla",
                skiprows=[1],
                usecols=["genus"]
            )

            for _, row in data.iterrows():
                genero = Genero.objects.filter(nombreGenero=row["genus"]).first()
                if not genero:
                    genero = Genero(nombreGenero=row["genus"])
                    genero.save()

            messages.success(request, "Los datos se cargaron exitosamente")
        except Exception as e:
            messages.error(request, f"Error al cargar el archivo: {str(e)}")

    return redirect("dashboard")



def element_detail(request, pk):
    element = get_object_or_404(especimen, pk=pk)
    familias = familia.objects.all()
    ordenes = Orden.objects.all()
    clases = Clase.objects.all()
    generos = Genero.objects.all()
    a = request.path
    rol = 0

    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    context = {
        "element": element,
        "familias": familias,
        "ordenes": ordenes,
        "clases": clases,
        "generos": generos,
        "a": a,
        "rol": rol,
    }
    return render(request, "paginaejemplar.html", context)


def aprobar_actividad(request, id):
    actividad = UserAction.objects.get(id_user_action=id)
    if actividad.tarea == "Archivar un ejemplar":
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
    return HttpResponseRedirect(reverse("dashboardCur"))


def darbaja_especimen(request, id):
    esp = especimen.objects.get(id=id)
    if request.user.groups.filter(name__in=["Auxiliar"]):
        NumeroCatalogo = esp.NumeroCatalogo
        TareaRealizada = 8
        Hora = datetime.now().time()
        Fecha = datetime.now().date()
        Descripcion = "Se Archivo el ejemplar " + NumeroCatalogo
        a = Actividades(
            NumeroCatalogo=NumeroCatalogo,
            TareaRealizada=TipoActividad.objects.get(id=TareaRealizada),
            Hora=Hora,
            Fecha=Fecha,
            Descripcion=Descripcion,
        )
        a.save()
        userAction = UserAction(
            user=request.user,
            tarea=TipoActividad.objects.get(id=TareaRealizada),
            ejemplar=NumeroCatalogo,
        )
        userAction.save()
        return HttpResponseRedirect(reverse("dashboardAux"))
    if request.user.groups.filter(name__in=["Pasante"]):
        esp = especimen.objects.get(id=id)
        esp.estado = False
        esp.save()
        return HttpResponseRedirect(reverse("dashboardPas"))
    if request.user.groups.filter(name__in=["Curador"]):
        esp = especimen.objects.get(id=id)
        esp.estado = False
        esp.save()
        return HttpResponseRedirect(reverse("dashboardCur"))
    esp = especimen.objects.get(id=id)
    esp.estado = False
    esp.save()
    return HttpResponseRedirect(reverse("dashboard"))


def AgregarActividad(request):
    if request.method == "POST":
        form = TipoActividadForm(request.POST)
        nombreactividad = request.POST.get("name")        
        if not nombreactividad:
            request.session["error"] = "No se agrego ninguna actividad debido a que no habia texto"
            return redirect("dashboard")

        max_id = TipoActividad.objects.all().aggregate(Max("id"))["id__max"]
        a = TipoActividad(id=max_id + 1, nombreactividad=nombreactividad)
        a.save()
        success = "Actividad agregada correctamente"
        return render(request, "dashboard.html", {"form": form, "success": success})
    else:
        form = TipoActividadForm()
        return render(request, "dashboard.html", {"form": form})


def EliminarActividad(request):
    actividad_id = request.GET.get("actividad_id")
    if actividad_id:
        actividad = get_object_or_404(TipoActividad, id=actividad_id)
        actividad.delete()
        return redirect("dashboard")
    else:
        actividades = TipoActividad.objects.all()
        return render(request, "dashboard.html", {"actividades": actividades})


def estado_usuarios(request):
    user = request.user
    if user.is_authenticated:
        rol = Rol.objects.get(user=user)
    usuarios = get_user_model().objects.all()
    return render(request, "desactivarUsuario.html", {"usuarios": usuarios, "rol": rol})


def desactivar_usuario(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse("dashboard"))


def activar_usuario(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse("dashboard"))


def update_text(request):
    if request.method == "POST":
        text = Text.objects.get(pk=2)
        text.content = request.POST["texto"]
        text.save()
        return redirect("dashboard")
    else:
        return render(request, "dashboard.html")


def estado_especimenes(request):
    user1 = request.user
    if user1.is_authenticated:
        rol = Rol.objects.get(user=user1)
    esp = especimen.objects.all()
    return render(request, "activarEspecimenes.html", {"especimenes": esp, "rol": rol})


def activar_especimen(request, id):
    esp = especimen.objects.get(id=id)
    esp.estado = True
    esp.save()
    return HttpResponseRedirect(reverse("dashboard"))


def elegir_texto(request):
    if request.method == "POST":
        if request.POST.get("optiontexto") == "option1":
            text = Text.objects.get(pk=2)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")

        elif request.POST.get("optiontexto") == "option2":
            text = Text.objects.get(pk=3)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")

        elif request.POST.get("optiontexto") == "option3":
            text = Text.objects.get(pk=4)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option4":
            text = Text.objects.get(pk=5)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option5":
            text = Text.objects.get(pk=6)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option6":
            text = Text.objects.get(pk=7)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option7":
            text = Text.objects.get(pk=8)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option8":
            text = Text.objects.get(pk=9)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")
        elif request.POST.get("optiontexto") == "option9":
            text = Text.objects.get(pk=10)
            text.content = request.POST["texto"]
            text.save()
            return redirect("dashboard")

        else:
            return HttpResponse("Invalid option")
    else:
        return redirect("dashboard.html")


def qr_code(request, data):
    # Crear el objeto QRCode
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    data = request.path
    print(data)
    qr.add_data("https://aulavirtual.unbosque.edu.co/")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer)
    response = HttpResponse(buffer.getvalue(), content_type="image/png")
    response["Content-Disposition"] = 'attachment; filename="qrcode.png"'
    return response


def qr_code1(request, pk):
    current_url = request.build_absolute_uri()

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    data = request.path
    print(data)
    qr.add_data(current_url[:-8])
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer)
    response = HttpResponse(buffer.getvalue(), content_type="image/png")
    response["Content-Disposition"] = 'attachment; filename="qrcode.png"'
    return response


def error_404(request, exception):
    return render(request, "404.html", {})




def export_data(request):
    columnas = [
        "occurrenceID",
        "basisOfRecord",
        "institutionCode",
        "collectionCode",
        "catalogNumber",
        "type",
        "modified",
        "language",
        "license",
        "rightsHolder",
        "accessRights",
        "bibliographicCitation",
        "references",
        "institutionID",
        "collectionID",
        "datasetID",
        "datasetName",
        "ownerInstitutionCode",
        "informationWithheld",
        "dataGeneralizations",
        "dynamicProperties",
        "occurrenceRemarks",
        "recordNumber",
        "recordedBy",
        "organismID",
        "individualCount",
        "organismQuantity",
        "organismQuantityType",
        "organismName",
        "sex",
        "lifeStage",
        "reproductiveCondition",
        "behavior",
        "establishmentMeans",
        "occurrenceStatus",
        "preparations",
        "disposition",
        "otherCatalogNumbers",
        "previousIdentifications",
        "associatedMedia",
        "associatedReferences",
        "associatedOccurrences",
        "associatedSequences",
        "associatedTaxa",
        "materialSampleID",
        "parentEventID",
        "eventID",
        "samplingProtocol",
        "sampleSizeValue",
        "sampleSizeUnit",
        "samplingEffort",
        "eventDate",
        "eventTime",
        "year",
        "month",
        "day",
        "verbatimEventDate",
        "habitat",
        "fieldNumber",
        "fieldNotes",
        "eventRemarks",
        "locationID",
        "higherGeographyID",
        "higherGeography",
        "continent",
        "waterBody",
        "islandGroup",
        "island",
        "country",
        "countryCode",
        "stateProvince",
        "county",
        "municipality",
        "locality",
        "verbatimLocality",
        "verbatimElevation",
        "minimumElevationInMeters",
        "maximumElevationInMeters",
        "minimumDepthInMeters",
        "maximumDepthInMeters",
        "locationRemarks",
        "verbatimCoordinates",
        "verbatimLatitude",
        "verbatimLongitude",
        "verbatimCoordinateSystem",
        "verbatimSRS",
        "decimalLatitude",
        "decimalLongitude",
        "geodeticDatum",
        "coordinateUncertaintyInMeters",
        "georeferencedBy",
        "georeferencedDate",
        "identifiedBy",
        "dateIdentified",
        "identificationReferences",
        "identificationVerificationStatus",
        "identificationRemarks",
        "identificationQualifier",
        "typeStatus",
        "taxonID",
        "scientificNameID",
        "acceptedNameUsageID",
        "scientificName",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "subgenus",
        "specificEpithet",
        "infraspecificEpithet",
        "taxonRank",
        "verbatimTaxonRank",
        "scientificNameAuthorship",
        "vernacularName",
        "nomenclaturalCode",
        "taxonomicStatus",
        "nomenclaturalStatus",
        "taxonRemarks",
        "Tipo de Montaje",
    ]

    df = pd.DataFrame(columns=columnas)
    column_name_mapping = {
        "catalogNumber": "NumeroCatalogo",
        "datasetName": "NombreDelConjuntoDatos",
        "institutionCode": "ComentarioRegistroBiologico",
        "recordedBy": "RegistradoPor",
        "individualCount": "NumeroIndividuo",
        "eventDate": "FechaEvento",
        "habitat": "Habitad",
        "stateProvince": "Departamento",
        "county": "Municipio",
        "identifiedBy": "IdentificadoPor",
        "dateIdentified": "FechaIdentificacion",
        "identificationReferences": "IdentificacionReferencias",
        "identificationRemarks": "ComentarioIdentificacion",
        "scientificName": "NombreCientificoComentarioRegistroBiologico",
        "class": "ClaseE",
        "order": "Orden",
        "genus": "Genero",
        "family": "Familia",
        "vernacularName": "NombreComun",
    }

    data = especimen.objects.all().values(
        "NumeroCatalogo",
        "NombreDelConjuntoDatos",
        "ComentarioRegistroBiologico",
        "RegistradoPor",
        "NumeroIndividuo",
        "FechaEvento",
        "Habitad",
        "Departamento",
        "Municipio",
        "IdentificadoPor",
        "FechaIdentificacion",
        "IdentificacionReferencias",
        "ComentarioIdentificacion",
        "NombreCientificoComentarioRegistroBiologico",
        "ClaseE",
        "Orden",
        "Genero",
        "Familia",
        "NombreComun",
    )
    data = list(data)

    for item in data:
        for key, value in column_name_mapping.items():
            item[key] = item.pop(value)
    df = df.append(pd.DataFrame(data), ignore_index=True)

    response = HttpResponse(content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="especimenes.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_data_cur(request, clase):
    columnas = [
        "occurrenceID",
        "basisOfRecord",
        "institutionCode",
        "collectionCode",
        "catalogNumber",
        "type",
        "modified",
        "language",
        "license",
        "rightsHolder",
        "accessRights",
        "bibliographicCitation",
        "references",
        "institutionID",
        "collectionID",
        "datasetID",
        "datasetName",
        "ownerInstitutionCode",
        "informationWithheld",
        "dataGeneralizations",
        "dynamicProperties",
        "occurrenceRemarks",
        "recordNumber",
        "recordedBy",
        "organismID",
        "individualCount",
        "organismQuantity",
        "organismQuantityType",
        "organismName",
        "sex",
        "lifeStage",
        "reproductiveCondition",
        "behavior",
        "establishmentMeans",
        "occurrenceStatus",
        "preparations",
        "disposition",
        "otherCatalogNumbers",
        "previousIdentifications",
        "associatedMedia",
        "associatedReferences",
        "associatedOccurrences",
        "associatedSequences",
        "associatedTaxa",
        "materialSampleID",
        "parentEventID",
        "eventID",
        "samplingProtocol",
        "sampleSizeValue",
        "sampleSizeUnit",
        "samplingEffort",
        "eventDate",
        "eventTime",
        "year",
        "month",
        "day",
        "verbatimEventDate",
        "habitat",
        "fieldNumber",
        "fieldNotes",
        "eventRemarks",
        "locationID",
        "higherGeographyID",
        "higherGeography",
        "continent",
        "waterBody",
        "islandGroup",
        "island",
        "country",
        "countryCode",
        "stateProvince",
        "county",
        "municipality",
        "locality",
        "verbatimLocality",
        "verbatimElevation",
        "minimumElevationInMeters",
        "maximumElevationInMeters",
        "minimumDepthInMeters",
        "maximumDepthInMeters",
        "locationRemarks",
        "verbatimCoordinates",
        "verbatimLatitude",
        "verbatimLongitude",
        "verbatimCoordinateSystem",
        "verbatimSRS",
        "decimalLatitude",
        "decimalLongitude",
        "geodeticDatum",
        "coordinateUncertaintyInMeters",
        "georeferencedBy",
        "georeferencedDate",
        "identifiedBy",
        "dateIdentified",
        "identificationReferences",
        "identificationVerificationStatus",
        "identificationRemarks",
        "identificationQualifier",
        "typeStatus",
        "taxonID",
        "scientificNameID",
        "acceptedNameUsageID",
        "scientificName",
        "kingdom",
        "phylum",
        "class",
        "order",
        "family",
        "genus",
        "subgenus",
        "specificEpithet",
        "infraspecificEpithet",
        "taxonRank",
        "verbatimTaxonRank",
        "scientificNameAuthorship",
        "vernacularName",
        "nomenclaturalCode",
        "taxonomicStatus",
        "nomenclaturalStatus",
        "taxonRemarks",
        "Tipo de Montaje",
    ]

    df = pd.DataFrame(columns=columnas)
    column_name_mapping = {
        "catalogNumber": "NumeroCatalogo",
        "datasetName": "NombreDelConjuntoDatos",
        "institutionCode": "ComentarioRegistroBiologico",
        "recordedBy": "RegistradoPor",
        "individualCount": "NumeroIndividuo",
        "eventDate": "FechaEvento",
        "habitat": "Habitad",
        "stateProvince": "Departamento",
        "county": "Municipio",
        "identifiedBy": "IdentificadoPor",
        "dateIdentified": "FechaIdentificacion",
        "identificationReferences": "IdentificacionReferencias",
        "identificationRemarks": "ComentarioIdentificacion",
        "scientificName": "NombreCientificoComentarioRegistroBiologico",
        "class": "ClaseE",
        "order": "Orden",
        "genus": "Genero",
        "family": "Familia",
        "vernacularName": "NombreComun",
    }

    data = especimen.objects.filter(ClaseE=clase).values(
        "NumeroCatalogo",
        "NombreDelConjuntoDatos",
        "ComentarioRegistroBiologico",
        "RegistradoPor",
        "NumeroIndividuo",
        "FechaEvento",
        "Habitad",
        "Departamento",
        "Municipio",
        "IdentificadoPor",
        "FechaIdentificacion",
        "IdentificacionReferencias",
        "ComentarioIdentificacion",
        "NombreCientificoComentarioRegistroBiologico",
        "ClaseE",
        "Orden",
        "Genero",
        "Familia",
        "NombreComun",
    )
    data = list(data)
    for item in data:
        for key, value in column_name_mapping.items():
            item[key] = item.pop(value)
    df = df.append(pd.DataFrame(data), ignore_index=True)
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename="especimenes.xlsx"'
    df.to_excel(response, index=False)
    return response

@login_required(login_url="redirect")
def change_password(request):
    rol = 0
    user = request.user
    if user.is_authenticated:
            rol = Rol.objects.get(user=user)
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Tu contraseña fue actualizada con éxito.')
            return redirect('home')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form': form})

def recover_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return redirect("recoverpass")

        user = get_user_model().objects.filter(email=email).first()

        if user:
            user.set_password(password1)
            user.save()
            messages.success(request, f"La contraseña del usuario {email} ha sido cambiada exitosamente.")
            return redirect("home")
        else:
            messages.error(request, "No existe un usuario con ese correo electrónico.")
            return redirect("recoverpass")
    else:
        return render(request, "recoverpass.html")