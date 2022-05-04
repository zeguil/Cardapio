from django.db import models

class Nutricional(models.Model):
    valorEnergetico = models.DecimalField(max_digits=4, decimal_places=1)
    carboidratos = models.DecimalField(max_digits=4, decimal_places=1)
    gordurasTotais = models.DecimalField(max_digits=4, decimal_places=1)
    gordurasSaturadas = models.DecimalField(max_digits=4, decimal_places=1)
    gordurasTrans = models.DecimalField(max_digits=4, decimal_places=1)
    fibraAlimentar = models.DecimalField(max_digits=4, decimal_places=1)
    sodio = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return str(self.id)
