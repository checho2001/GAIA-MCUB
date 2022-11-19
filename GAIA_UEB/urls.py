from django.contrib import admin
from django.urls import path
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('inicio/', admin.site.urls),
    path('', IndexView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
