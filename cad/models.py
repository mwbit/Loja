from django.db import models

class Usuario(models.Model):
    nm_usuario = models.CharField(max_length=70)
    nivel = models.CharField(max_length=2)
    senha = models.CharField(max_length=8)
