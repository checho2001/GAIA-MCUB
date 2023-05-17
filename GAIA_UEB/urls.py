from django.contrib import admin
from django.urls import path, include
from users.views import (
    IndexView,
    Galry,
    Dashboard,
    Dashboard_Aux,
    load_data,
    Dashboard_Pas,
    Dashboard_Cur,
    PerfilU,
    registroActividad,
    registerE,
    EjemplarP,
    CambioContrasenia,
    Not_Logged,
    update_ejemplar,
    export_data_cur,
    export_data,
    RecoverPasswordView,
)
from users.views import (
    IndexView,
    Quienessomos,
    Galry,
    Dashboard,
    Dashboard_Aux,
    load_data,
    Dashboard_Pas,
    Dashboard_Cur,
    PerfilU,
    registroActividad,
    registerE,
    EjemplarP,
    CambioContrasenia,
    Not_Logged,
    register,
    update_ejemplar,
    element_detail,
    EliminarActividad,
)
from django.views.defaults import page_not_found
from users import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    path("", IndexView.as_view(), name="home"),
    path("index/", IndexView.as_view(), name="home"),
    path("nosotros/", Quienessomos.as_view(), name="quienessomos"),
    path("login/", views.login, name="login"),
    path("galery/", Galry.as_view(), name="galery"),
    path("redirect/", Not_Logged.as_view(), name="redirect"),
    path("cambio/", CambioContrasenia.as_view(), name="cambio"),
    path("register/", views.register, name="register"),
    path("registerE/", views.registerE, name="registerE"),
    path("dash/", Dashboard.as_view(), name="dashboard"),
    path("dashAux/", Dashboard_Aux.as_view(), name="dashboardAux"),
    path("dashPas/", Dashboard_Pas.as_view(), name="dashboardPas"),
    path("dashCur/", Dashboard_Cur.as_view(), name="dashboardCur"),
    path("perfilU/", PerfilU.as_view(), name="perfilU"),
    path("informe/", views.registroActividad, name="registroActividad"),
    path("ejemplar/", EjemplarP.as_view(), name="Ejemplar"),
    path("updateE/<int:id>", update_ejemplar.as_view(), name="updateE"),
    path(
        "updateE/updateEjemplar/<int:id>",
        views.update_record_ejemplar,
        name="updateEjemplar",
    ),
    path("dardebaja/<int:id>", views.darbaja_especimen, name="darbajaE"),
    path("activar/<int:id>", views.activar_especimen, name="ActivarE"),
    path("UpdateUser/", views.update_aux_curatoria, name="UpdateU"),
    path("DesactivarUser/", views.estado_usuarios, name="DesactivarUser"),
    path("desactivarU/<int:id>", views.desactivar_usuario, name="DesactivarU"),
    path("activarU/<int:id>", views.activar_usuario, name="ActivarU"),
    path("ActivarEspecimen/", views.estado_especimenes, name="ActivarEspecimen"),
    path("logout", views.custom_logout, name="logout"),
    path("elegir", views.elegir, name="elegir"),
    path("AgregarActividad/", views.AgregarActividad, name="AgregarActividad"),
    path("update_text/", views.update_text, name="update_text"),
    path("elegirtexto", views.elegir_texto, name="elegirtexto"),
    path("load_data/", load_data, name="load_data"),
    path("paginaejemplar/<int:pk>/", element_detail, name="element_detail"),
    path("dashCur/aprobar/<int:id>", views.aprobar_actividad, name="aprobarA"),
    path("galery/familia/<str:nombre>", views.galery_familia, name="galeryF"),
    path("galery/genero/<str:nombre>", views.galery_genero, name="galeryG"),
    path("galery/clase/<str:nombre>", views.galery_clase, name="galeryC"),
    path("galery/orden/<str:nombre>", views.galery_orden, name="galeryO"),
    path("qr_code/<str:data>/", views.qr_code, name="qr_code"),
    path("paginaejemplar/<int:pk>/qr_code/", views.qr_code1, name="qr_code1"),
    path("EliminarActividad/", views.EliminarActividad, name="EliminarActividad"),
    path('load_data_clase/', views.load_data_clase, name='load_data_clase'),
    path('load_data_orden/', views.load_data_orden, name='load_data_orden'),
    path('load_data_genero/', views.load_data_genero, name='load_data_genero'),
    path('load_data_familia/', views.load_data_familia, name='load_data_familia'),
    path(
        "obtener_usuario/<int:id_usuario>/",
        views.obtener_usuario,
        name="obtener_usuario",
    ),
    path('changepass/', views.change_password, name='change_password'),
    path(
        "exportar-datos-cur/<str:clase>",
        views.export_data_cur,
        name="exportar_datos_cur",
    ),
    path("exportar-datos/", views.export_data, name="exportar_datos"),
     path('recoverpass/', RecoverPasswordView.as_view(), name='recover_password'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "users.views.error_404"
