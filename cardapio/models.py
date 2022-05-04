from django.db import models
from nutricional.models import Nutricional

class Cardapio(models.Model):
    nome = models.CharField(max_length=40)
    valor = models.FloatField()
    detalhes = models.TextField()
    foto = models.ImageField(upload_to='pratos/', null=True, blank=True)
    nutricional = models.ForeignKey(
        Nutricional, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

