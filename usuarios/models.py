from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    rol = models.CharField(
        max_length=50,
        choices=[('admin', 'Administrador'), ('empleado', 'Empleado')],
        default='empleado'
    )

    def __str__(self):
        return f"{self.username} ({self.rol})"
