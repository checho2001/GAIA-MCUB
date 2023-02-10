from django import forms
from .models import User
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
    ROLES =[(1,"Auxiliar"),(2,"Pasante"),(3,"Curador"),(4,"Otro")]
    
    
    rol = forms.ChoiceField(
        choices = ROLES, )    
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
    Actividaes =[(1,"Determinación de las muestras a familia, género o especie"),
    (2,"Conservación del material"),(3,"Montaje del material en seco"),
    (4,"Registro de los datos en Excel"),(5,"Organizar la colección por orden alfabético"),
    (6,"Revisión bibliográfica"),(7,"Curación de los ejemplares")]
    TareaRealizada = forms.ChoiceField(
        choices = Actividaes, )


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
    NumeroIndividuo = forms.IntegerField( widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    FechaEvento = forms.CharField( widget=DateInput(  
        attrs={'class': 'form-control',}))
    Habitad= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    Departamento= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    Municipio= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
                'required' : True,
                'class' : 'form-control',
                }
            ))
    IdentificadoPor= forms.CharField(max_length=500, widget=forms.TextInput(
            attrs= {
               
                'required' : True,
                'class' : 'form-control',
                }
            ))
    FechaIdentificacion = forms.CharField( widget=DateInput(  
        attrs={'class': 'form-control',}))
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