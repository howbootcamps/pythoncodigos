"""
How Bootcamps - Stone - /código[s]
Data: 14/04/2022
Autor: Henrique Junqueira Branco
Enunciado: Encapsulamento - Venda e Imposto
"""

from impostos import COFINS, ICMS, IPI, ISS, Imposto


class Venda:
    def __init__(self, valor_bruto: float, imp: Imposto):
        self.valor_bruto = valor_bruto
        self.tributo = imp

    def calcula_valor_liquido(self):
        return self.tributo.calcula(self.valor_bruto)


v1 = Venda(10000.00, ICMS())
v2 = Venda(1000, IPI())
v3 = Venda(124091, ISS())
v4 = Venda(1231, COFINS())

print(v1.calcula_valor_liquido())
