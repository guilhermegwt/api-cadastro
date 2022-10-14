from django.db import models
from django.contrib.auth.models import User

def password_generator():
    password = User.objects.make_random_password(length=12)
    return str(password)

class Cadastro(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=12, default=password_generator)
    dt_nascimento = models.DateField()
