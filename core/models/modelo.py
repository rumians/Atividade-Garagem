from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f'({self.nome}) - {self.id} - {self.marca.upper()}'