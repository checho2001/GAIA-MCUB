from django.contrib import admin
from django.urls import path
from users.views import IndexView,Galry,Dashboard,PerfilU,registro,registroActividad

from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('login/', views.login, name='login'),
    path('galery/', Galry.as_view(),name="galery"),
    path("register/", views.register, name="register"),
    path("registerE/", registro.as_view(), name="registerE"),
    path('dash/', Dashboard.as_view(),name="dashboard"),
    path('perfilU/', PerfilU.as_view(),name="perfilU"),
    path('informe/',  views.registroActividad,name="registroActividad"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
