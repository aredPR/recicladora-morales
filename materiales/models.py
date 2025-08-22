from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['id']


class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['id']  # evita el warning de paginación


class RegistroMaterial(models.Model):
    """Registro de movimientos de material."""

    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="registros"
    )
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.material.nombre} - {self.cantidad_kg}kg ({self.fecha.date()})"
