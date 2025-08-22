from django.contrib import admin
from .models import Venta, Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email')
    search_fields = ('nombre', 'telefono', 'email')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'material', 'cantidad_kg', 'precio_unitario', 'total', 'fecha', 'registrado_por')
    search_fields = ('cliente__nombre', 'material__nombre')
    list_filter = ('fecha', 'cliente')
