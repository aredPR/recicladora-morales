from rest_framework import serializers
from .models import Venta, Cliente
from materiales.models import Material

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class VentaSerializer(serializers.ModelSerializer):
    cliente  = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    material = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all())

    class Meta:
        model = Venta
        fields = "__all__"
        read_only_fields = ("total", "fecha", "registrado_por")
