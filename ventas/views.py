import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Venta, Cliente
from .serializers import VentaSerializer, ClienteSerializer
from usuarios.permissions import IsAdminOrReadCreateOnly

class VentaFilter(django_filters.FilterSet):
    fecha_min = django_filters.IsoDateTimeFilter(field_name="fecha", lookup_expr="gte")
    fecha_max = django_filters.IsoDateTimeFilter(field_name="fecha", lookup_expr="lte")
    cliente   = django_filters.NumberFilter(field_name="cliente_id")
    material  = django_filters.NumberFilter(field_name="material_id")

    class Meta:
        model = Venta
        fields = ["cliente", "material", "fecha_min", "fecha_max"]

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all().order_by("-fecha")
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = VentaFilter
    search_fields = ["cliente__nombre", "material__nombre"]
    ordering_fields = ["fecha", "total", "cantidad_kg"]
    ordering = ["-fecha"]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("nombre")
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]
