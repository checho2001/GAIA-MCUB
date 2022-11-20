from django import forms
from .models import User
from django.core.exceptions import ValidationError
from .models import Rol
from django.contrib.auth.forms import UserCreationForm
class loginForm(forms.Form):
    username = forms.EmailField(
        error_messages={'required':'Por favor ingrese su correo electronico para continuar'},
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
    
    

    def clean_username(self):
        mail = self.cleaned_data['username']
        if User.objects.filter(email=mail).count():
            pass
        else:
            raise ValidationError(('Correo no valido - Este correo no se encuentra registrado, por favor vuelva a intentarlo'))

        return mail

class NewUserForm(forms.Form):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("correo", "contrasenia", "contrasenia2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
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
    

	     