from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'telefono', 'rol')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('rol',)
