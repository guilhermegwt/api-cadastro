# pylint: disable=E1101, C0114

from rest_framework import viewsets
from cadastro.models import Cadastro
from cadastro.serializers import CadastroSerializer

class CadastroViewSet(viewsets.ModelViewSet):
    """
    View utilizada para processar das requisições dos usuários
    """
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
