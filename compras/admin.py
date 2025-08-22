from django.contrib import admin
from .models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'material', 'cantidad_kg', 'precio_unitario', 'total', 'fecha', 'registrado_por')
    search_fields = ('proveedor__nombre', 'material__nombre')
    list_filter = ('fecha', 'proveedor')
