from django.contrib import admin
from django.urls import path
from users.views import IndexView,Galry,Dashboard,Dashboard_Aux,Dashboard_Pas,Dashboard_Cur,PerfilU,registroActividad,registerE,EjemplarP,CambioContrasenia,Not_Logged,register,update_ejemplar

from users import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='home'),
    path('login/', views.login, name='login'),
    path('galery/', Galry.as_view(),name="galery"),
    path('redirect/', Not_Logged.as_view(),name="redirect"),
    path('cambio/', CambioContrasenia.as_view(),name="cambio"),
    path("register/", views.register, name="register"),
    path("registerE/", views.registerE, name="registerE"),
    path('dash/', Dashboard.as_view(),name="dashboard"),
    path('dashAux/', Dashboard_Aux.as_view(),name="dashboardAux"),
    path('dashPas/', Dashboard_Pas.as_view(),name="dashboardPas"),
    path('dashCur/', Dashboard_Cur.as_view(),name="dashboardCur"),
    path('perfilU/', PerfilU.as_view(),name="perfilU"),
    path('informe/',  views.registroActividad,name="registroActividad"),
    path('ejemplar/',  EjemplarP.as_view(),name="Ejemplar"),
    path('logout', views.custom_logout, name='logout'),
    path('dashAux/updateE/<int:id>', update_ejemplar.as_view(), name='updateE'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
