from django.contrib import admin
from django.urls import path
from users.views import IndexView,Galry

from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('login/', views.login, name='login'),
    path('galery/', Galry.as_view()),
    path("register/", views.register_request, name="registerUser"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
