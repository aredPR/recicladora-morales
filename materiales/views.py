from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Material, Proveedor, RegistroMaterial
from .serializers import (
    MaterialSerializer,
    ProveedorSerializer,
    RegistroMaterialSerializer,
)
from usuarios.permissions import IsAdminOrReadCreateOnly  

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]  

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]


class RegistroMaterialViewSet(viewsets.ModelViewSet):
    queryset = RegistroMaterial.objects.all().order_by("-fecha")
    serializer_class = RegistroMaterialSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]
