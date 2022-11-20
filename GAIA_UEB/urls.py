from django.contrib import admin
from django.urls import path
from users.views import IndexView,Galry,Dashboard

from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('login/', views.login, name='login'),
    path('galery/', Galry.as_view()),
    path("register/", views.register, name="register"),
    path('dash/', Dashboard.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
