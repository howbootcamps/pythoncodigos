"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos.
Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado.
Escreva um programa que demonstre o uso da sua função.
"""


def calcula_tarifa(dist_km: float) -> float:
    # dist_km * 1_000 -> transforma km em metros
    # / 140 (para cada 140 metros)
    # * 0.25 multiplica pelo valor em R$
    return 4 + dist_km * 1_000 / 140 * 0.25


print(
    f"Para uma disância de 0,14 km (1.400 metros) o valor total da corrida é: {calcula_tarifa(0.14)}"
)
