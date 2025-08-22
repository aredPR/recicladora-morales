from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Material, Proveedor, RegistroMaterial
from .serializers import (
    MaterialSerializer,
    ProveedorSerializer,
    RegistroMaterialSerializer,
)
from usuarios.permissions import IsAdminOrReadCreateOnly  

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all().order_by('id')
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('id')
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

class RegistroMaterialViewSet(viewsets.ModelViewSet):
    queryset = RegistroMaterial.objects.all().order_by("-fecha")
    serializer_class = RegistroMaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]
