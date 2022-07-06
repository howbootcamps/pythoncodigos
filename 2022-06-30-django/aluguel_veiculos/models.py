from django.db import models


class Cliente(models.Model):
    PESSOA_FISICA = 'PF'
    PESSOA_JURIDICA = 'PJ'

    CLIENTE_CHOICES = [
        (PESSOA_FISICA, 'Fisica'),
        (PESSOA_JURIDICA, 'Juridica'),
    ]
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cpf = models.CharField(max_length=11, null=True)
    cnpj = models.CharField(max_length=14, null=True)
    tipo = models.CharField(max_length=2, choices=CLIENTE_CHOICES, default=PESSOA_FISICA)

    def __str__(self) -> str:
        return self.nome


class Veiculo(models.Model):
    TIPO_AUTOMOVEL = "VL"
    TIPO_CAMINHAO = "VP"

    VEICULO_CHOICES = [
        (TIPO_AUTOMOVEL, "Automovel"),
        (TIPO_CAMINHAO,"Caminhao")
    ]

    placa = models.CharField(max_length=7)
    km = models.FloatField()
    carga = models.FloatField()
    bagageiro = models.IntegerField()
    portas = models.IntegerField()
    tipo = models.CharField(max_length=2, choices=VEICULO_CHOICES, default=TIPO_AUTOMOVEL)


class Aluguel(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    km_rodado = models.FloatField()

    class Meta():
        verbose_name_plural = 'Alugueis'
