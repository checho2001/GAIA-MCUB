from django import forms
from .models import Users
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
        if Users.objects.filter(email=mail).count():
            pass
        else:
            raise ValidationError(('Correo no valido - Este correo no se encuentra registrado, por favor vuelva a intentarlo'))

        return mail

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Users
		fields = ("correo", "contrasenia", "contrasenia2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user