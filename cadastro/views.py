from rest_framework import viewsets
from cadastro.models import Usuario
from cadastro.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    View utilizada para processar das requisições dos usuários
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
