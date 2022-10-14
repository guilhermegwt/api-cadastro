from rest_framework import serializers
from cadastro.models import Cadastro

class CadastroSerializer(serializers.ModelSerializer):
    """
    Serializer utilizado transformar dados em um formato que pode ser armazenado ou transmitido e,
    então, reconstruído
    """
    class Meta:
        """
        Modelo e campos do Serializer
        """
        model = Cadastro
        fields = '__all__'
