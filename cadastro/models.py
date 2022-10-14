# pylint: disable=C0114

from django.db import models
from django.contrib.auth.models import User

def password_generator():
    """
    Gerador de senhas
    """
    password = User.objects.make_random_password(length=12)
    return str(password)

class Cadastro(models.Model):
    """
    Modelo do dado que será gerenciado pela API
    """
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=12, default=password_generator)
    dt_nascimento = models.DateField()
