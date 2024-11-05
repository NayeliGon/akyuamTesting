from django.contrib import admin
from django.urls import path
from myapp import views  # Asegúrate de importar las vistas de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Vista para la URL raíz
]
