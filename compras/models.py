from django.db import models
from materiales.models import Proveedor, Material
from usuarios.models import Usuario

class Compra(models.Model):
    # 👇 proveedor opcional
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="compras"
    )
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="compras")
    cantidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total = self.cantidad_kg * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        prov = self.proveedor.nombre if self.proveedor else "Sin proveedor"
        return f"Compra #{self.id} - {prov} ({self.fecha.date()})"
