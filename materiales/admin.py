from django.contrib import admin
from .models import Material, Proveedor, RegistroMaterial

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "telefono")
    search_fields = ("nombre",)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio_kg")
    search_fields = ("nombre",)


@admin.register(RegistroMaterial)
class RegistroMaterialAdmin(admin.ModelAdmin):
    list_display = ("id", "material", "cantidad_kg", "fecha")
    list_filter = ("material", "fecha")
