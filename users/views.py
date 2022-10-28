from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import * 
from django.contrib import auth
from django.urls import reverse   
def login(request):
    contador = 1
    usuario_intentando = ''

    if 'contador' in request.session:
        contador = request.session['contador']
    else:
        request.session['contador'] = 1
    
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if 'u_actual' in request.session:
                usuario_intentando = request.session['u_actual']
            else:
                request.session['u_actual'] = email
                usuario_intentando = email
            
            if usuario_intentando == email:

                if contador <= 3:

                    user = auth.authenticate(email=email, password=password)

                    if user is not None and user.is_active and not user.bloqueado:
                        # Correct password, and the user is marked "active"
                        auth.login(request, user)
                        # Redirect to a success page.
                        return HttpResponseRedirect(reverse('citas:dashboard'))
                    elif user is not None and user.bloqueado:
                        return render(request, 'registration/login.html', {'mensaje_error':'Su usuario se encuentra actualmente bloqueado, por favor comuniquese con el administrador', 'form':form})
                    else:
                        request.session['contador'] = contador+1
                        return render(request, 'registration/login.html', {'mensaje_error':'Su usuario o contraseña son incorrectos o su correo no se encuentra verificado, por favor intente de nuevo', 'form':form})
                else:
                    aBloquear = Users.objects.get(email=email)
                    aBloquear.bloqueado = True
                    aBloquear.save()
                    request.session['contador'] = 1
                    return render(request, 'registration/login.html', {'mensaje_error':'Su usuario ha llegado al limite de intentos permitidos, por lo cual ha sido bloqueado, por favor contactese con el administrador.', 'form':form})
            else:
                request.session['usua_actual'] = email
                request.session['contador'] = 1
                contador = 1

                if contador <= 3:

                    user = auth.authenticate(email=email, password=password)

                    if user is not None and user.is_active and not user.bloqueado:
                        # Correct password, and the user is marked "active"
                        auth.login(request, user)
                        # Redirect to a success page.
                        return HttpResponseRedirect(reverse('citas:dashboard'))
                    elif user is not None and user.bloqueado:
                        return render(request, 'registration/login.html', {'mensaje_error':'Su usuario se encuentra actualmente bloqueado, por favor comuniquese con el administrador', 'form':form})
                    else:
                        request.session['contador'] = contador+1
                        return render(request, 'registration/login.html', {'mensaje_error':'Su usuario o contraseña son incorrectos o su correo no se encuentra verificado, por favor intente de nuevo', 'form':form})
                else:
                    aBloquear = Users.objects.get(email=email)
                    aBloquear.bloqueado = True
                    aBloquear.save()
                    request.session['contador'] = 1
                    return render(request, 'registration/login.html', {'mensaje_error':'Su usuario ha llegado al limite de intentos permitidos, por lo cual ha sido bloqueado, por favor contactese con el administrador.', 'form':form})

    else:
        form = LoginForm()
    
    return render(request, 'pagina/login.html', {'form':form})