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
    tipo = models.CharField(
        max_length=2, choices=CLIENTE_CHOICES, default=PESSOA_FISICA)

    def __str__(self) -> str:
        return self.nome
