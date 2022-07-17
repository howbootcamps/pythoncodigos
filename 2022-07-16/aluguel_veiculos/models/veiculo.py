from django.db import models


class Veiculo(models.Model):
    TIPO_AUTOMOVEL = "VL"
    TIPO_CAMINHAO = "VP"

    VEICULO_CHOICES = [
        (TIPO_AUTOMOVEL, "Automovel"),
        (TIPO_CAMINHAO, "Caminhao")
    ]

    placa = models.CharField(max_length=7)
    km = models.FloatField()
    carga = models.FloatField()
    bagageiro = models.IntegerField()
    portas = models.IntegerField()
    tipo = models.CharField(
        max_length=2, choices=VEICULO_CHOICES, default=TIPO_AUTOMOVEL)

    def __str__(self) -> str:
        return self.placa