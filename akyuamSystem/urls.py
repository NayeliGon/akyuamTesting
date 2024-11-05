from django.contrib import admin
from django.urls import path, include
from sistema import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Usa la vista genérica de Django
]
