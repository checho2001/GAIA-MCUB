"""
Module Name: forms.py
Description: This module contains the Django forms for the application.
"""
from datetime import date
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
import datetime
from django import forms
from django.db import DatabaseError
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import FormView
from .models import (
    User,
    departamento,
    municipio,
    TipoActividad,
    especimen,
    Clase,
    familia,
    Orden,
    Genero,
    Rol    )
class CustomUser(forms.Form):
    """
    Representa un formulario para registrar a un usuario.
    """
    nombre = forms.CharField(
        error_messages={"required": "Por favor ingresa un nombre valido"},
        strip=True,
        widget=forms.TextInput(
            attrs={
                "required": True,
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )
    apellido = forms.CharField(
        error_messages={"required": "Por favor ingresa un apellido valido"},
        widget=forms.TextInput(
            attrs={
                "required": True,
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "required": True,
                "style": "height: 80PX;",
                "class": "form-control",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "required": True,
                "name": "passUser",
                "style": "height: 80PX;",
                "class": "form-control",
            }
        )
    )
    username = forms.CharField(
        error_messages={"required": ""},
        strip=True,
        widget=forms.TextInput(
            attrs={
                "required": True,
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )
    ROLES = []

    for rol in Rol.objects.all():
        ROLES.append((rol.id, rol.nombrerol))

    rol = forms.ChoiceField(
        choices=ROLES,
        widget=forms.Select(
            attrs={
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )
    AREA = []
    for clase in Clase.objects.all():
        AREA.append((clase.id, clase.nombreClase))

    area = forms.ChoiceField(
        choices=AREA,
        widget=forms.Select(
            attrs={
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )

    def clean(self):
        """
        Representa un clean method para realizar validaciones.
        """
        cleaned_data = super().clean()
        correo = cleaned_data.get("correo")
        nombre = cleaned_data.get("nombre")
        username = cleaned_data.get("username")
        apellido = cleaned_data.get("apellido")
        password = cleaned_data.get("password")

        try:
            if correo and "@unbosque.edu.co" not in correo:
                raise forms.ValidationError("El correo debe contener @unbosque.edu.co")
        except forms.ValidationError as error:
            self.add_error("correo", error)

        try:
            if User.objects.filter(email=correo).count():
                raise forms.ValidationError(
                    _("Correo no valido, este correo ya se encuentra registrado, "
                    "por favor vuelva a intentarlo")
                )

        except forms.ValidationError as error:
            self.add_error("correo", error)

        try:
            if nombre and not re.match("^[a-zA-Z]*$", nombre):
                raise forms.ValidationError(
                    "Nombre inválido, debe contener sólo letras."
                )
        except forms.ValidationError as error:
            self.add_error("nombre", error)

        try:
            if username and not re.match("^[a-zA-Z\d]*$", username):
                raise forms.ValidationError(
                    "Usuario inválido, debe contener sólo letras y números."
                )
        except forms.ValidationError as error:
            self.add_error("username", error)

        try:
            if apellido and not re.match("^[a-zA-Z]*$", apellido):
                raise forms.ValidationError(
                    "Apellido inválido, debe contener sólo letras."
                )
        except forms.ValidationError as error:
            self.add_error("apellido", error)

        try:
            if password:
                if len(password) < 8:
                    raise forms.ValidationError(
                        "La contraseña debe tener al menos 8 caracteres."
                    )
                elif len(password) > 16:
                    raise forms.ValidationError(
                        "La contraseña no debe tener más de 16 caracteres."
                    )
                elif not re.search("[A-Z]", password):
                    raise forms.ValidationError(
                        "La contraseña debe tener al menos una letra mayúscula."
                    )
                elif not re.search("[0-9]", password):
                    raise forms.ValidationError(
                        "La contraseña debe tener al menos un número."
                    )
        except forms.ValidationError as error:
            self.add_error("password", error)

        return cleaned_data


class loginForm(forms.Form):
    """
    Representa un el login form para entrar al sistema.
    """
    username = forms.CharField(
        error_messages={"required": "Por favor ingresa un correo valido"},
        strip=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite su correo",
                "required": True,
                "class": "form-control",
                "style": "height: 70px;",
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Ingrese su contraseña",
                "required": True,
                "name": "passUser",
                "class": "form-control",
                "style": "height: 70px;",
            }
        )
    )
    captcha = CaptchaField()

    def clean_username(self):
        """
        Representa un clean method para realizar validaciones.
        """
        mail = self.cleaned_data["username"]
        if "@unbosque.edu.co" not in mail:
            raise forms.ValidationError("El correo debe contener  unbosque.edu.co")

        return mail


class DateInput(forms.DateInput):
    """
    Representa un formulario para fecha.
    """
    input_type = "date"


class TimeInput(forms.TimeInput):
    """
    Representa un formulario para hora.
    """
    input_type = "time"

class ActividadesForm(forms.Form):
    """
    Representa un formulario para las actividades.
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(ActividadesForm, self).__init__(*args, **kwargs)

    TAREAS = []

    for tarea in TipoActividad.objects.all():
        TAREAS.append((tarea.id, tarea.nombreactividad))

    TareaRealizada = forms.ChoiceField(
        choices=TAREAS,
        widget=forms.Select(
            attrs={
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )

    Hora = forms.TimeField(
        widget=TimeInput(
            attrs={
                "class": "form-control",
                "style": "height: 80PX;",
            }
        )
    )
    Fecha = forms.DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "style": "height: 80PX;",
            }
        )
    )
    Descripcion = forms.CharField(
        error_messages={"required": "Por favor ingresa una descripción valida"},
        strip=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite la descripcion",
                "required": True,
                "class": "form-control",
                "style": "height: 80PX;",
            }
        ),
    )

    def clean_fecha(self):
        """
        Representa un validador para la fecha.
        """
        fecha = self.cleaned_data["Fecha"]
        if fecha.year < 2000:
            raise ValidationError("La fecha es demasiado antigua")
        if fecha > datetime.date.today():
            raise ValidationError("La fecha no puede ser en el futuro")
        return fecha

    def clean_Descripcion(self):
        """
        Representa un validador para la descripción.
        """
        descripcion = self.cleaned_data["Descripcion"]
        if not descripcion:
            raise ValidationError("El campo descripción no puede estar vacío")
        return descripcion

    def clean(self):
        """
        Representa un validator para los dos clean anteriores.
        """
        cleaned_data = super().clean()
        try:
            self.clean_fecha()
        except ValidationError as e:
            self.add_error("Fecha", e)
        return cleaned_data

class EjemplarForm(forms.Form):
    """
    Representa un form para los especimenes.
    """
    NumeroCatalogo = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.TextInput(
            attrs={
                "required": True,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    CONJUNTODEDATOS = [
        "Colección de Exhibición de Anfibios",
        "Colección de Exhibición de Aves",
        "Colección de exhibición de Reptiles",
        "Colección de exhibición de Mammalia",
        "Colección de exhibición de Myriapoda",
        "Colección de referencia de Arachnida",
        "Colección de exhibición de Mollusca",
    ]

    NombreDelConjuntoDatos = forms.ChoiceField(
        choices=[(i, i) for i in CONJUNTODEDATOS],
        widget=forms.Select(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )

    COMENTARIO_CHOICES = [
        ("1", "Encontrado muerto en una salida de campo académica"),
        ("2", "Donación"),
        ("3", "Otro"),
    ]
    ComentarioRegistroBiologico = forms.CharField(
        max_length=500,
        widget=forms.Select(
            choices=COMENTARIO_CHOICES,
            attrs={
                "class": "form-control",
                "style": "height: 80px;",
            },
        ),
    )
    ComentarioRegistroBiologico_otro = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "style": "height: 80px;",
                "required": False,
            }
        ),
    )
    RegistradoPor = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    NumeroIndividuo = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "style": "height: 80px;",
                "step": "1",
                "min": "0",
                "max": "1000",
                "required": False,
            }
        )
    )
    FechaEvento = forms.DateField(
        widget=DateInput(
            attrs={
                "class": "form-control",
                "style": "height: 80px;",
            }
        )
    )
    Habitad = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    DEPARTAMENTOS = []

    for departamentos in departamento.objects.all():
        DEPARTAMENTOS.append((departamentos.id, departamentos.nombre))

    Departamento = forms.ChoiceField(
        choices=DEPARTAMENTOS,
        widget=forms.Select(
            attrs={
                "required": False,
                "default": 0,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    MUNICIPIOS = []

    for municipio in municipio.objects.all():
        MUNICIPIOS.append((municipio.id, municipio.municipio))

    Municipio = forms.ChoiceField(
        choices=MUNICIPIOS,
        widget=forms.Select(
            attrs={
                "required": False,
                "default": 1,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    IdentificadoPor = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    FechaIdentificacion = forms.DateField(
        widget=DateInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        )
    )
    IdentificacionReferencias = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    ComentarioIdentificacion = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    NombreCientificoComentarioRegistroBiologico = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    CLASES = []
    ORDENES = []
    GENEROS = []
    FAMILIAS = []
    for clase in Clase.objects.all():
        CLASES.append((clase.id, clase.nombreClase))
    for orden in Orden.objects.all():
        ORDENES.append((orden.id, orden.nombreOrden))
    for genero in Genero.objects.all():
        GENEROS.append((genero.id, genero.nombreGenero))
    for fam in familia.objects.all():
        FAMILIAS.append((fam.id, fam.nombreFamilia))

    ClaseE = forms.ChoiceField(
        choices=CLASES,
        widget=forms.Select(
            attrs={
                "default": 1,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    Orden = forms.ChoiceField(
        choices=ORDENES,
        widget=forms.Select(
            attrs={
                "default": 1,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    Genero = forms.ChoiceField(
        choices=GENEROS,
        widget=forms.Select(
            attrs={
                "default": 1,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    Familia = forms.ChoiceField(
        choices=FAMILIAS,
        widget=forms.Select(
            attrs={
                "default": 1,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )
    NombreComun = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "required": False,
                "class": "form-control",
                "style": "height: 80px;",
            }
        ),
    )

    Image = forms.ImageField(
        required=False,
        error_messages={
            "required": "Seleccione la imagen del ejemplar ",
            "invalid": "El formato es erroneo",
        },
    )

    def clean_NumeroCatalogo(self):
        """
        Representa un validador para el número de catalogo.
        """
        numero_catalogo = self.cleaned_data.get("NumeroCatalogo")
        if numero_catalogo is None:
            return "MCUB-E-"
        numero_catalogo_con_prefijo = "MCUB-E-{}".format(numero_catalogo)

        try:
            if especimen.objects.filter(
                NumeroCatalogo=numero_catalogo_con_prefijo
            ).exists():
                raise forms.ValidationError("El número de catálogo ya está registrado.")
        except DatabaseError:
            raise forms.ValidationError("El número de catálogo ya está registrado.")

        return numero_catalogo_con_prefijo

    def clean_Fecha_evento(self):
        """
        Representa un validador para la fecha.
        """
        fecha_evento = self.cleaned_data["FechaEvento"]
        if fecha_evento > datetime.date.today():
            raise ValidationError("La fecha no puede ser en el futuro")
        return fecha_evento

    def clean_Fecha_Identificacion(self):
        """
        Representa un validador para la fecha.
        """
        fecha_I = self.cleaned_data["FechaIdentificacion"]
        if fecha_I > datetime.date.today():
            raise ValidationError("La fecha no puede ser en el futuro")
        return fecha_I

    def clean(self):
        """
        Representa un validador
        """
        cleaned_data = super().clean()
        comentario = cleaned_data.get("ComentarioRegistroBiologico")
        otro_comentario = cleaned_data.get("ComentarioRegistroBiologico_otro")
        if comentario == "otro" and not otro_comentario:
            raise forms.ValidationError(
                "Debe especificar un comentario si selecciona 'Otro'."
            )
        try:
            self.clean_Fecha_evento()
        except ValidationError as e:
            self.add_error("FechaEvento", e)
        try:
            self.clean_Fecha_Identificacion()

        except ValidationError as e:
            self.add_error("FechaIdentificacion", e)

        return cleaned_data

class Update(forms.Form):
    """
    Representa un form para actualizar el usuario .
    """
    USUARIOS = []

    for useri in User.objects.all():
        USUARIOS.append((useri.id, useri.username))

    username = forms.ChoiceField(
        choices=USUARIOS,
        widget=forms.Select(
            attrs={
                "style": "height: 80PX;",
                "class": "form-control",
            }
        ),
    )

    nombre = forms.CharField(
        required=False,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite su nombre",
                "class": "form-control",
                "style": "height: 80PX;",
            }
        ),
    )
    apellido = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite su apellido",
                "class": "form-control",
                "style": "height: 80PX;",
            }
        ),
    )
    correo = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Digite su correo",
                "class": "form-control",
                "style": "height: 80PX;",
            }
        ),
    )

    ROLES = []

    for rol in Rol.objects.all():
        ROLES.append((rol.id, rol.nombrerol))

    rol = forms.ChoiceField(
        choices=ROLES,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "style": "height: 80PX;",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        user_id = self.initial.get("username", None)
        if user_id:
            user = User.objects.get(id=user_id)
            self.fields["nombre"].initial = user.nombre
            self.fields["apellido"].initial = user.apellido
            self.fields["correo"].initial = user.email

    def clean_nombre(self):
        """
        Representa un validator para el nombre .
        """
        nomb = self.cleaned_data["nombre"]

        if nomb and not re.match("^[a-zA-Z]*$", nomb):
            raise forms.ValidationError("Nombre inválido, debe contener sólo letras.")

        return nomb

    def clean_username(self):
        """
        Representa un validator para el username .
        """
        usernm = self.cleaned_data["username"]

        if not re.match("^[a-zA-Z\d]*$", usernm):
            raise forms.ValidationError(
                "Usuario inválido, debe contener sólo letras y números."
            )

        return usernm

    def clean_apellido(self):
        """
        Representa un validator para el apellido .
        """
        apel = self.cleaned_data["apellido"]

        if apel and not re.match("^[a-zA-Z]*$", apel):
            raise forms.ValidationError("Apellido inválido, debe contener sólo letras.")

        return apel

class desactivarUsuario(forms.Form):
    """
    Representa un form para desactivar  el usuario .
    """
    USUARIOS = []
    u = User.objects.filter(estado=True)
    for useri in User.objects.all():
        USUARIOS.append((useri.id, useri.username))
    username = forms.ChoiceField(
        choices=USUARIOS,
        widget=forms.Select(
            attrs={
                "default": 1,
                "class": "form-control",
            }
        ),
    )

class TipoActividadForm(forms.Form):
    """
    Representa un form para el tipo de actividad.
    """
    nombreactividad = forms.CharField(
        error_messages={"required": "Por favor ingresa una actividad valida"},
        widget=forms.TextInput(
            attrs={
                "required": True,
                "class": "form-control",
            }
        ),
    )


class TextForm(forms.Form):
    """
    Representa un form para desactivar  el usuario .
    """
    content = forms.CharField(label="New Text", max_length=255)




class CustomPasswordChangeForm(PasswordChangeForm):
    """
    Representa un form para cambiar la contraseña .
    """
    old_password = forms.CharField(
        label=_("Contraseña actual"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )

    new_password1 = forms.CharField(
        label=_("Nueva contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
  


    )

    new_password2 = forms.CharField(
        label=_("Confirmar nueva contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )

    def clean_new_password1(self):
        """
        Representa un validator para la contraseña .
        """
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise ValidationError("La contraseña debe contener al menos 8 caracteres.")
        if password1.isnumeric():
            raise ValidationError("La contraseña no puede ser completamente numérica.")
        return password1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control',
            'id': 'PassActual',
            'placeholder': 'Contraseña Actual',
        })

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'NewPass',
            'placeholder': 'Nueva Contraseña',
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'ConfPass',
            'placeholder': 'Confirmar Contraseña',
        })

    def save(self, commit=True):
        return super().save(commit)
    
class RecoverPasswordForm(forms.Form):
    """
    Representa un form para cambiar la contraseña .
    """
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Contraseña Nueva",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=("La contraseña no puede ser demasiado similar a otras información personal."
                    "La contraseña debe contener al menos 8 caracteres."
                    "La contraseña no puede ser completamente numérica.")
    )
    password2 = forms.CharField(
        label="Confirmación de la contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class RecoverPasswordView(FormView):
    """
    Representa un form para cambiar la contraseña .
    """
    template_name = "recoverpass.html"
    form_class = RecoverPasswordForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        user = get_user_model().objects.get(email=email)
        user.set_password(password)
        user.save()
        messages.success(self.request, f"La contraseña del usuario {email} ha sido actualizada exitosamente.")
        return super().form_valid(form)
