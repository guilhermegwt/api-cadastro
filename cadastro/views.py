# pylint: disable=E1101

from rest_framework import viewsets
from cadastro.models import Cadastro
from cadastro.serializers import CadastroSerializer

class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
