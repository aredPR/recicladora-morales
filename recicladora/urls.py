"""
URL configuration for recicladora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers

# importa tus viewsets si ya creaste la API
from usuarios.views import UsuarioViewSet
from compras.views import CompraViewSet
from ventas.views import VentaViewSet, ClienteViewSet
from materiales.views import (
    ProveedorViewSet,
    MaterialViewSet,
    RegistroMaterialViewSet,
)

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'materiales', MaterialViewSet)
# router.register(r'registros-materiales', RegistroMaterialViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API REST
    path('', include('frontend.urls')),  # Frontend
    path("login/", auth_views.LoginView.as_view(template_name="frontend/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
