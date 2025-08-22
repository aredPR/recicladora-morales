from django.http import HttpResponse
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer

def index(request):
    return HttpResponse("Módulo de usuarios funcionando 🚀")

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

