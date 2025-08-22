from rest_framework import serializers
from .models import Material, Proveedor, RegistroMaterial

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class RegistroMaterialSerializer(serializers.ModelSerializer):
    material = serializers.PrimaryKeyRelatedField(
        queryset=Material.objects.all()
    )

    class Meta:
        model = RegistroMaterial
        fields = "__all__"
