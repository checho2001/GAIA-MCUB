from django import forms
from .models import Users
from django.core.exceptions import ValidationError
from .models import Rol

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
        if Users.objects.filter(email=mail).count():
            pass
        else:
            raise ValidationError(('Correo no valido - Este correo no se encuentra registrado, por favor vuelva a intentarlo'))

        return mail

class registerUserForm(forms.Form):
        nombre = forms.CharField( error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,widget=forms.TextInput(
            attrs= {'placeholder':'Digite su nombre',
                'required' : True,
                'class' : '',
                }
            ))
        apellido = forms.CharField( error_messages={'required':'Por favor ingresa un nombre valido'},
        strip = True,
        widget=forms.TextInput(
            attrs= {
                'placeholder':'Digite su nombre',
                'required' : True,
                'class' : '',
                }
            ))
        ROLES = []
        ROLES.append((1,"Curador"))
        for roles in Rol.objects.filter(estado = True):
                ROLES.append((roles.idrol, roles.nombrerol))
        rol = forms.ChoiceField(
        choices = ROLES,
        widget=forms.Select(
            attrs= {
                'default' : 1,
                'required' : True,
                'class' : '',
                }
            )
        )
        password =  forms.CharField(
        widget=forms.PasswordInput(
                attrs= {
                'placeholder':'Ingrese su contraseña',
                'required' : True,
                'name' : 'passUser',
                'class' : '',
                }
            )
        )
        correo = forms.EmailField(
        widget=forms.EmailInput(
            attrs= {
                'placeholder':'Example@email.com',
                'required' : True,
                'class' : '',
                }
            )
        )