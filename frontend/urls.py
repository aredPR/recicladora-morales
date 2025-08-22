from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("compras/", views.compras, name="compras"),
    path("ventas/", views.ventas, name="ventas"),
    path("materiales/", views.materiales, name="materiales"),
    path("proveedores/", views.proveedores, name="proveedores"),
    path("clientes/", views.clientes, name="clientes"), 
    path("reportes/", views.reportes, name="reportes"),
    path("configuracion/", views.configuracion, name="configuracion"),
]
