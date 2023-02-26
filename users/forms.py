from django import forms
from .models import User,departamento, municipio, TipoActividad
from django.core.exceptions import ValidationError
from .models import Rol
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django import forms

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
                'default' : 1,
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
                'placeholder':'Digite su nombre',
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
    NumeroCatalogo = forms.CharField(
        error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite El numero de catalogo',
                'required' : True,
                'class' : 'form-control',
                }
            )
        )
    TAREAS = []
    
    for tarea in TipoActividad.objects.all():
        TAREAS.append((tarea.id,tarea.nombreactividad))     
       
    TareaRealizada = forms.ChoiceField(
        choices = TAREAS,  widget=forms.Select(
            attrs= {
                'default' : 1,
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
        error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite la descripcion',
                'required' : True,
                'class' : 'form-control',
                }
            )
        )        
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
    NombreDelConjuntoDatos = forms.CharField(max_length=500,  widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
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
    MUNICIPIOS = []
    
    for departamentos in departamento.objects.all():
        DEPARTAMENTOS.append((departamentos.id,departamentos.nombre))

    for municipio in municipio.objects.all():
        MUNICIPIOS.append((municipio.id,municipio.municipio))     
    
    Departamento = forms.ChoiceField(
        choices = DEPARTAMENTOS,
        widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
                }
            )
        )
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
    TipoClases =[(1,"Aves")]
    
    
    ClaseE = forms.ChoiceField(
        choices = TipoClases, ) 
    NombreComun = forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                
                'required' : True,
                'class' : 'form-control',
                }
            ))
    '''
    Image = forms.ImageField(
        required=False,
        error_messages={'required':'Please select the image of the cover', 'invalid':'The format of your image is invalid, please try again'},
    )
    '''
