from django import forms
from .models import Users
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    email = forms.EmailField( error_messages={'required':'Por favor ingrese su correo electronico para continuar'},widget=forms.TextInput(attrs= {'placeholder':'Correo Institucional','required' : True,'name' : 'correoU',}))
    contrasenia = forms.CharField (max_length = 70,widget=forms.PasswordInput(attrs= {'placeholder':'Contraseña'}))
def cleancorreo(self):
    mail = self.cleaned_data['email']
    if Users.objects.filter(email=mail).count():
            pass
    else:
            raise ValidationError(('Correo no valido - Este correo no se encuentra registrado, por favor vuelva a intentarlo'))

    return mail
