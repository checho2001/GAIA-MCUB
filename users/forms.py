from django import forms
from .models import User,departamento, municipio, TipoActividad,especimen,Clase,familia,Orden,Genero
from django.core.exceptions import ValidationError
from .models import Rol, Area
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django import forms
from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse_lazy
from django.conf import settings
import datetime
import re
from django.db import DatabaseError
from datetime import date

class CustomUser(forms.Form):
    nombre = forms.CharField( 
        
        error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su nombre',
                'required' : True,
                'class' : 'form-control',

                }
            )
        
        )
    apellido = forms.CharField(
        error_messages={'required':'Por favor ingresa un apellido valido'},
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su apellido',
                'required' : True,
                'class' : 'form-control',
                }
            )
        )
    correo = forms.EmailField(
        widget=forms.EmailInput( 
        attrs= {
                'placeholder':'Digite su correo',
                'required' : True,
                'class' : 'form-control',
                }
            
            )
        )
    password =  forms.CharField(
        widget=forms.PasswordInput(
                attrs= {
                'placeholder':'Ingrese su contraseña',
                'required' : True,
                'name' : 'passUser',
                'class' : 'form-control',
                }
            )
        )
    username = forms.CharField(
        error_messages={'required':''},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su usuario',
                'required' : True,
                'class' : 'form-control',
                }
            )
        )        
    ROLES =[]
        
    for rol in Rol.objects.all():
        ROLES.append((rol.id,rol.nombrerol))     
    
    rol = forms.ChoiceField(
        choices = ROLES,  widget=forms.Select(
            attrs= {
               'style': 'height: 70px;',
                
                'class' : 'form-control',
                }
            ))
    AREA = []
    for clase in Clase.objects.all():
        AREA.append((clase.id, clase.nombreClase))

    area = forms.ChoiceField(
        choices = AREA,  widget=forms.Select(
            attrs= {
                'style': 'height: 70px;',
                'class' : 'form-control',
                }
            ))

    def clean_correo(self):
        mail = self.cleaned_data['correo']
        if "@unbosque.edu.co" not in mail:   
            raise forms.ValidationError("El correo debe contener  unbosque.edu.co")
        if User.objects.filter(email=mail).count():
            raise ValidationError(_('Correo no valido - Este correo ya se encuentra registrado, por favor vuelva a intentarlo'))
        return mail      
    def clean_nombre(self):
            nomb = self.cleaned_data['nombre']
            for l in nomb:
                if l.isnumeric():
                    raise ValidationError(_('Nombre invalido - Tu nombre no puede contener numeros'))
    
            return nomb
    def clean_apellido(self):
            apel = self.cleaned_data['apellido']
            for l in apel:
                if l.isnumeric():
                    raise ValidationError(_('Apellido invalido - Tu apellido no puede contener numeros'))
            return apel
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        elif len(password) > 16:
            raise forms.ValidationError("La contraseña no debe tener más de 16 caracteres.")
        elif not re.search("[A-Z]", password):
            raise forms.ValidationError("La contraseña debe tener al menos una letra mayúscula.")
        elif not re.search("[0-9]", password):
            raise forms.ValidationError("La contraseña debe tener al menos un número.")
        
        return password
class loginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required':'Por favor ingresa un correo valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su correo',
                'required' : True,
                'class' : 'form-control',
                'style': 'height: 70px;',
                }
            )
        )   
    password =  forms.CharField(
        widget=forms.PasswordInput(
                attrs= {
                'placeholder':'Ingrese su contraseña',
                'required' : True,
                'name' : 'passUser',
                'class' : 'form-control',
                'style': 'height: 70px;',
                }
            )
        )
    captcha = CaptchaField()
    def clean_username(self):
        mail = self.cleaned_data['username']
        if "@unbosque.edu.co" not in mail:   
            raise forms.ValidationError("El correo debe contener  unbosque.edu.co")
    
        return mail  
    

class DateInput(forms.DateInput):
    input_type='date'
class TimeInput(forms.TimeInput):
    input_type='time'       


class ActividadesForm(forms.Form):


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ActividadesForm, self).__init__(*args, **kwargs)
    TAREAS = []
    
    for tarea in TipoActividad.objects.all():
        TAREAS.append((tarea.id,tarea.nombreactividad))     
       
    TareaRealizada = forms.ChoiceField(
        choices = TAREAS,  widget=forms.Select(
            attrs= {
                'style': 'height: 70px;',
                'class' : 'form-control',
                }
            ))


    Hora = forms.TimeField(   widget=TimeInput(
        
        attrs={'class': 'form-control','style': 'height: 70px;',}
    )

        )
    Fecha = forms.DateField(   widget=DateInput(  
        attrs={'class': 'form-control','style': 'height: 80px;font-size: 30px;',})
        )
    Descripcion = forms.CharField(
        error_messages={'required':'Por favor ingresa una descripción valida'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite la descripcion',
                'required' : True,
                'class' : 'form-control',
                }
            )
        ) 
    def clean_fecha(self):
        fecha = self.cleaned_data['Fecha']
        if fecha.year < 2000:
            raise ValidationError('La fecha es demasiado antigua')
        if fecha > datetime.date.today():
            raise ValidationError('La fecha no puede ser en el futuro')
        return fecha
    def clean(self):
        cleaned_data = super().clean()
        try:
            self.clean_fecha()
        except ValidationError as e:
            self.add_error('Fecha', e)
        return cleaned_data
class Especimen_Form(forms.Form):
    NumeroCatalogo = forms.CharField(max_length=500,required=True,  widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    NombreDelConjuntoDatos = forms.CharField(max_length=500,  widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))


class EjemplarForm(forms.Form):
    NumeroCatalogo = forms.CharField(max_length=500,required=True,  widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    CONJUNTODEDATOS = [    "Colección de Exhibición de Anfibios",    "Colección de Exhibición de Aves",    "Colección de exhibición de Reptiles",    "Colección de exhibición de Mammalia",    "Colección de exhibición de Myriapoda",    "Colección de referencia de Arachnida","Colección de exhibición de Mollusca"]

    NombreDelConjuntoDatos = forms.ChoiceField(
        choices=[(i, i) for i in CONJUNTODEDATOS],
        widget=forms.Select(
            attrs={
                'class': 'form-control','style': 'height: 70px;',
            }
        )
    )
    

    ComentarioRegistroBiologico = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    RegistradoPor = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    NumeroIndividuo =  forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    FechaEvento =  forms.DateField(   widget=DateInput(  
        attrs={'class': 'form-control','style': 'height: 70px;',})
        )
    Habitad= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    DEPARTAMENTOS= []

    for departamentos in departamento.objects.all():
        DEPARTAMENTOS.append((departamentos.id,departamentos.nombre))

    Departamento = forms.ChoiceField(
        choices = DEPARTAMENTOS,
        widget=forms.Select(
            attrs= {
                'default' : 0,
                'class' : 'form-control','style': 'height: 70px;',
                }
            )
        )
    MUNICIPIOS= []

    for municipio in municipio.objects.all():
        MUNICIPIOS.append((municipio.id, municipio.municipio))

    Municipio = forms.ChoiceField(
        choices = MUNICIPIOS,
        widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control','style': 'height: 70px;',
                }
            )
        )
    IdentificadoPor= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
               
                'required' : True,
                'class' : 'form-control',
                }
            ))
    FechaIdentificacion =  forms.DateField(   widget=DateInput(  
        attrs={'class': 'form-control','style': 'height: 70px;',})
        )
    IdentificacionReferencias = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    ComentarioIdentificacion = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    NombreCientificoComentarioRegistroBiologico = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    CLASES = []
    ORDENES= []
    GENEROS= []
    FAMILIAS= []
    for clase in Clase.objects.all():
        CLASES.append((clase.id,clase.nombreClase))
    for orden in Orden.objects.all():
        ORDENES.append((orden.id,orden.nombreOrden))
    for genero in Genero.objects.all():
        GENEROS.append((genero.id,genero.nombreGenero))
    for fam in familia.objects.all():
        FAMILIAS.append((fam.id,fam.nombreFamilia))        
    
    ClaseE = forms.ChoiceField(
        choices = CLASES, widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control','style': 'height: 70px;',
                }
            )) 
    Orden = forms.ChoiceField(
        choices = ORDENES, widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control','style': 'height: 70px;',
                }
            )) 
    Genero = forms.ChoiceField(
        choices = GENEROS,widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control','style': 'height: 70px;',
                }
            ) ) 
    Familia = forms.ChoiceField(
        choices = FAMILIAS,widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control','style': 'height: 70px;',
                }
            ) ) 
    NombreComun = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                
                'required' : True,
                'class' : 'form-control',
                }
            ))
    
    Image = forms.ImageField(
        required=False,
        error_messages={'required':'Seleccione la imagen del ejemplar ', 'invalid':'El formato es erroneo'},
    )
    def clean_NumeroCatalogo(self):
        data = self.cleaned_data['NumeroCatalogo']
        try:
         if especimen.objects.filter(NumeroCatalogo=data).exists():
             raise forms.ValidationError('El número de catálogo ya está registrado.')
        except DatabaseError:
            raise forms.ValidationError('El número de catálogo ya está registrado.')
        return data

class Update(forms.Form):
    USUARIOS = []

    for useri in User.objects.all():
        USUARIOS.append((useri.id, useri.username))
    username = forms.ChoiceField(
        choices = USUARIOS,
        widget=forms.Select(
            attrs= {
                 'style': 'height: 70px;',
                'class' : 'form-control',
                }
            )
        )

    nombre = forms.CharField( 
        
        error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su nombre',
                'required' : True,
                'class' : 'form-control',

                }
            )
        
        )
    apellido = forms.CharField(
        error_messages={'required':'Por favor ingresa un apellido valido'},
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su apellido',
                'required' : True,
                'class' : 'form-control',
                }
            )
        )
    correo = forms.EmailField(
        widget=forms.EmailInput( 
        attrs= {
                'placeholder':'Digite su correo',
                'required' : True,
                'class' : 'form-control',
                }
            
            )
        )
    
    ROLES =[]
        
    for rol in Rol.objects.all():
        ROLES.append((rol.id,rol.nombrerol))     
    
    rol = forms.ChoiceField(
        choices = ROLES,  widget=forms.Select(
            attrs= {
                 'style': 'height: 70px;',
                'class' : 'form-control',
                }
            ))    
    def clean_correo(self):
        mail = self.cleaned_data['correo']
        if "@unbosque.edu.co" not in mail:   
            raise forms.ValidationError("El correo debe contener  unbosque.edu.co")
        return mail      
    def clean_nombre(self):
            nomb = self.cleaned_data['nombre']
            for l in nomb:
                if l.isnumeric():
                    raise ValidationError(_('Nombre invalido - Tu nombre no puede contener numeros'))
    
            return nomb
    def clean_apellido(self):
            apel = self.cleaned_data['apellido']
            for l in apel:
                if l.isnumeric():
                    raise ValidationError(_('Apellido invalido - Tu apellido no puede contener numeros'))
            return apel
    
class desactivarUsuario(forms.Form):

    USUARIOS = []
    u = User.objects.filter(estado = True)
    for useri in User.objects.all():
        USUARIOS.append((useri.id, useri.username))
    username = forms.ChoiceField(
        choices = USUARIOS,
        widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
                }
            )
        )

class TipoActividadForm(forms.Form):

       
        nombreactividad = forms.CharField(
        error_messages={'required':'Por favor ingresa una actividad valida'},
        widget=forms.TextInput(
            attrs= {
                
                'required' : True,
                'class' : 'form-control',
                }
            )
        )


class TextForm(forms.Form):

       
       content = forms.CharField(label='New Text', max_length=255)
        
class ContactForm(forms.Form):
    nombre = forms.CharField(error_messages={'required':'Por favor ingresa un nombre valido'},
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su Nombre',
                'required' : True,
                'class' : 'form-control',
                }
            ))
    correo = forms.EmailField(widget=forms.EmailInput( 
        attrs= {
                'placeholder':'Digite su correo',
                'required' : True,
                'class' : 'form-control',
                }
            
            ))
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Digite su Mensaje',
            'class': 'form-control',
            'rows': 5,
            'required': True,
        }),
        error_messages={'required': 'Por favor ingresa un mensaje válido'}
    )

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Contraseña actual"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )

    new_password1 = forms.CharField(
        label=_("Nueva contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=_("La contraseña no puede ser demasiado similar a otras información personal."
                    "La contraseña debe contener al menos 8 caracteres."
                    "La contraseña no puede ser completamente numérica."),
    )

    new_password2 = forms.CharField(
        label=_("Confirmar nueva contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )

    def clean_new_password1(self):
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

    def send_email(self, email):
        subject = 'Confirmación de cambio de contraseña'
        message = f'Hola {self.user.username}, se ha cambiado la contraseña exitosamente'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)

    def save(self, commit=True):
        response = super().save(commit)

        # Send email confirmation
        self.send_email(self.user.email)

        return response