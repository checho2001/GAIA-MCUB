from django.contrib import admin
from django.urls import path
from users.views import IndexView,Galry,Dashboard,PerfilU,registro,registroActividad,registerE,EjemplarP

from users import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='home'),
    path('login/', views.login, name='login'),
    path('galery/', Galry.as_view(),name="galery"),
    path("register/", views.register, name="register"),
    path("registerE/", views.registerE, name="registerE"),
    path('dash/', Dashboard.as_view(),name="dashboard"),
    path('perfilU/', PerfilU.as_view(),name="perfilU"),
    path('informe/',  views.registroActividad,name="registroActividad"),
    path('ejemplar/',  EjemplarP.as_view(),name="Ejemplar"),
    path('logout', views.custom_logout, name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
