from django import forms
from .models import User,departamento, municipio, TipoActividad,especimen,Clase,familia,Orden,Genero
from django.core.exceptions import ValidationError
from .models import Rol, Area
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django import forms
from captcha.fields import CaptchaField
import datetime

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
        
        attrs={'class': 'form-control',}
    )

        )
    Fecha = forms.DateField(   widget=DateInput(  
        attrs={'class': 'form-control',})
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
                'class': 'form-control',
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
        attrs={'class': 'form-control',})
        )
    Habitad= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    DEPARTAMENTOS = []

    for departamentos in departamento.objects.all():
        DEPARTAMENTOS.append((departamentos.id,departamentos.nombre))

    Departamento = forms.ChoiceField(
        choices = DEPARTAMENTOS,
        widget=forms.Select(
            attrs= {
                'default' : 0,
                'class' : 'form-control',
                }
            )
        )
    MUNICIPIOS = []

    for municipio in municipio.objects.all():
        MUNICIPIOS.append((municipio.id, municipio.municipio))

    Municipio = forms.ChoiceField(
        choices = MUNICIPIOS,
        widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
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
        attrs={'class': 'form-control',})
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
                'class' : 'form-control',
                }
            )) 
    Orden = forms.ChoiceField(
        choices = ORDENES, widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
                }
            )) 
    Genero = forms.ChoiceField(
        choices = GENEROS,widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
                }
            ) ) 
    Familia = forms.ChoiceField(
        choices = FAMILIAS,widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
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