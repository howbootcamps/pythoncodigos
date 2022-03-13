"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário
"""

entrada = {1: "vermelho", 2: "azul", 3: "marrom"}

saida = dict()

for chave, valor in entrada.items():
    saida[chave] = len(valor)

print(saida)
