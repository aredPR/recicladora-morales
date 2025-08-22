from rest_framework import serializers
from .models import Compra
from materiales.models import Proveedor, Material

class CompraSerializer(serializers.ModelSerializer):
    # Aceptar y devolver IDs de FK
    proveedor = serializers.PrimaryKeyRelatedField(queryset=Proveedor.objects.all())
    material  = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())

    class Meta:
        model = Compra
        fields = "__all__"
        read_only_fields = ("total", "fecha", "registrado_por")
