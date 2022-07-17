import datetime
from django.db import models
from aluguel_veiculos.models.cliente import Cliente
from aluguel_veiculos.models.veiculo import Veiculo


class Aluguel(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_retirada = models.DateField(default=datetime.date.today)
    data_devolucao = models.DateField(default=datetime.date.today)
    km_rodado = models.FloatField()
    valor = models.FloatField(null=True, default=0)

    class Meta():
        verbose_name_plural = 'Alugueis'
