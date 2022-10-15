from rest_framework import serializers
from cadastro.views import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer utilizado transformar dados em um formato que pode ser armazenado ou transmitido e,
    então, reconstruído
    """
    class Meta:
        """
        Modelo e campos do Serializer
        """
        model = Usuario
        fields = '__all__'
