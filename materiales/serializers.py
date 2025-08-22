from rest_framework import serializers
from .models import Material, Proveedor, RegistroMaterial

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'nombre', 'descripcion', 'precio_kg']

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'telefono', 'email', 'direccion']

class RegistroMaterialSerializer(serializers.ModelSerializer):
    material = serializers.PrimaryKeyRelatedField(
        queryset=Material.objects.all()
    )

    class Meta:
        model = RegistroMaterial
        fields = "__all__"
