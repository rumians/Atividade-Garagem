from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, blank=True, null=True)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, blank=True, null=True)
    acessorios = models.ManyToManyField('Acessorio', blank=True)
    
    def __str__(self):
        return f"({self.id}) ({self.cor}) ({self.ano})"