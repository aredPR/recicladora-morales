from django.db import models
from materiales.models import Material
from usuarios.models import Usuario

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="ventas")
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.cantidad_kg * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre} ({self.fecha.date()})"
