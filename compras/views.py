import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from rest_framework.permissions import IsAuthenticated
from .models import Compra
from .serializers import CompraSerializer
from usuarios.permissions import IsAdminOrReadCreateOnly

class CompraFilter(django_filters.FilterSet):
    fecha_min = django_filters.IsoDateTimeFilter(field_name="fecha", lookup_expr="gte")
    fecha_max = django_filters.IsoDateTimeFilter(field_name="fecha", lookup_expr="lte")
    proveedor = django_filters.NumberFilter(field_name="proveedor_id")
    material  = django_filters.NumberFilter(field_name="material_id")

    class Meta:
        model = Compra
        fields = ["proveedor", "material", "fecha_min", "fecha_max"]

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by("-fecha")
    serializer_class = CompraSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadCreateOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CompraFilter
    search_fields = ["proveedor__nombre", "material__nombre"]
    ordering_fields = ["fecha", "total", "cantidad_kg"]
    ordering = ["-fecha"]
