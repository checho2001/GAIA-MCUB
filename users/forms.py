from django import forms
from .models import User,departamento, municipio, TipoActividad,especimen,Clase,familia,Orden,Genero
from django.core.exceptions import ValidationError
from .models import Rol, Area
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django import forms
from captcha.fields import CaptchaField

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
    AREA = []
    for clase in Clase.objects.all():
        AREA.append((clase.id, clase.nombreClase))

    area = forms.ChoiceField(
        choices = AREA,  widget=forms.Select(
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


    CATALOGO = []
    for useri in especimen.objects.all():
        CATALOGO.append((useri.id, useri.NumeroCatalogo))
    NumeroCatalogo = forms.ChoiceField(
        choices = CATALOGO,  widget=forms.Select(
            attrs= {
                'default' : 1,
                'class' : 'form-control',
                }
            ))  
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
        error_messages={'required':'Please select the image of the cover', 'invalid':'The format of your image is invalid, please try again'},
    )
class Update(forms.Form):
    USUARIOS = []

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
    


class TipoActividadForm(forms.ModelForm):
    class Meta:
        model = TipoActividad
        fields = ['nombreactividad']