from django.contrib import admin
from .models import Proveedor, Material

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "telefono")
    search_fields = ("nombre",)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio_kg")
    search_fields = ("nombre",)
