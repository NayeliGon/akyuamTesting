from django.contrib import admin
from django.urls import path, include
from sistema import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  
     # Si tienes otras rutas para manejar el login o vistas, asegúrate de incluirlas
    # path('login/', auth_view.LoginView.as_view(), name='login'),  # ejemplo
]
