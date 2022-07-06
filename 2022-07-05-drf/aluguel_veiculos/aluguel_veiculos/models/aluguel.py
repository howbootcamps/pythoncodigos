from django.db import models
from aluguel_veiculos.models.cliente import Cliente
from aluguel_veiculos.models.veiculo import Veiculo


class Aluguel(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    km_rodado = models.FloatField()

    class Meta():
        verbose_name_plural = 'Alugueis'
