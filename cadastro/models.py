from django.db import models

class Cadastro(models.Model):
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=20)
    dt_nascimento = models.DateField()