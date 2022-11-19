from django import forms
from .models import Users
from django.core.exceptions import ValidationError
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
            raise ValidationError(_('Correo no valido - Este correo no se encuentra registrado, por favor vuelva a intentarlo'))

        return mail

   