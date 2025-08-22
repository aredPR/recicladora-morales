from rest_framework import serializers
from .models import Compra
from materiales.models import Proveedor, Material

class CompraSerializer(serializers.ModelSerializer):
    # Aceptar y devolver IDs de FK
    proveedor = serializers.PrimaryKeyRelatedField(
        queryset=Proveedor.objects.all(),
        allow_null=True, required=False   # 👈 opcional
    )
    material  = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())

    # Campos de solo lectura para mostrar nombres en la UI
    proveedor_nombre = serializers.SerializerMethodField(read_only=True)
    material_nombre  = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"
        read_only_fields = ("total", "fecha", "registrado_por", "proveedor_nombre", "material_nombre")

    def get_proveedor_nombre(self, obj):
        return obj.proveedor.nombre if obj.proveedor else None

    def get_material_nombre(self, obj):
        return obj.material.nombre if obj.material else None
