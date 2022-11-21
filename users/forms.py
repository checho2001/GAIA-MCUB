from django import forms
from .models import User
from django.core.exceptions import ValidationError
from .models import Rol

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
                'placeholder':'Example@email.com',
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
    ROLES =[(1,"Auxiliar"),(2,"Pasante"),(3,"Curador"),(4,"Otro")]
    
    
    rol = forms.ChoiceField(
        choices = ROLES, )    

def clean_nombre(self):
        nomb = self.cleaned_data['nombre']
        for l in nomb:
            if l.isnumeric():
                raise ValidationError(_('Nombre invalido - Tu nombre no puede contener numeros'))
        
        nombre = nomb
        partes=nombre.split(" ")
        reconstruido = ""
        for p in partes:
            if p!='':
                reconstruido+=p+" "
        nombre = reconstruido.strip()

        if not (nombre.replace(" ", "").isalpha()):
            raise ValidationError(_('Nombre invalido - Tu nombre no puede contener numeros o caracteres especiales'))
        
        nomb = nombre.upper()
        
        return nomb
def clean_apellido(self):
        apel = self.cleaned_data['apellido']
        for l in apel:
            if l.isnumeric():
                raise ValidationError(_('Apellido invalido - Tu apellido no puede contener numeros'))
        
        partes = apel.split(" ")

        if len(partes) < 2:
            raise ValidationError(_('Apellido invalido - Debes tener al menos dos apellidos para poder registrarte'))
        
        nombre = apel
        partes=nombre.split(" ")
        reconstruido = ""
        for p in partes:
            if p!='':
                reconstruido+=p+" "
        nombre = reconstruido.strip()

        if not (nombre.replace(" ", "").isalpha()):
            raise ValidationError(_('Apellido invalido - Tu apellido no puede contener numeros o caracteres especiales'))
        
        apel = nombre.upper()
        
        return apel
    
def clean_correo(self):
        mail = self.cleaned_data['correo']
        if User.objects.filter(email=mail).count():
            raise ValidationError(_('Correo no valido - Este correo ya se encuentra registrado, por favor vuelva a intentarlo'))
        return mail      
class loginForm(forms.Form):
    username = forms.CharField(
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
    
    

def clean_correo(self):
        mail = self.cleaned_data['correo']
        if User.objects.filter(email=mail).count():
            raise ValidationError(_('Correo no valido - Este correo ya se encuentra registrado, por favor vuelva a intentarlo'))
        return mail     


class NewEspecimen(forms.Form):
    NumeroCatalogo = forms.CharField(max_length=255,required=True)
    NombreDelConjuntoDatos = forms.CharField(max_length=500)
    ComentarioRegistroBiologico = forms.CharField(max_length=500)
    RegistradoPor = forms.CharField(max_length=500)
    NumeroIndividuo = forms.IntegerField()
    FechaEvento = forms.DateTimeField()
    Habitad= forms.CharField(max_length=500)
    Departamento= forms.CharField(max_length=500)
    Municipio= forms.CharField(max_length=500)
    IdentificadoPor= forms.CharField(max_length=500)
    FechaIdentificacion = forms.DateTimeField()
    IdentificacionReferencias = forms.CharField(max_length=500)
    ComentarioIdentificacion = forms.CharField(max_length=500)
    NombreCientificoComentarioRegistroBiologico = forms.CharField(max_length=500)
    Clase = forms.CharField(max_length=500)
    Orden = forms.CharField(max_length=500)
    Familia = forms.CharField(max_length=500)
    Genero = forms.CharField(max_length=500)
    NombreComun = forms.CharField(max_length=500)
    

	     