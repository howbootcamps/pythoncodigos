"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. 
"""

entrada = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}

# Coletando todos os valores do dicionário e transformando-os em uma lista
valores = list(entrada.values())

# Valores máximo e mínimo da lista
valor_max = max(valores)
valor_min = min(valores)

# Índices (posições) máximo e mínimo dos respectivos valores
indice_max = valores.index(valor_max)
indice_min = valores.index(valor_min)

# A partir do índice, conseguimos extrair o nome transformando as chaves dos dicionários em uma lista
# Passo a passo de list(entrada.keys())[indice_max]
# entrada.keys() -> retorna um objeto keys a partir do dicionário
# transformamos esse objeto em lista -> list(entrada.keys())
# da lista de nomes, coletamos o índice correspondente aos valores máximos e mínimos
print(f"Nota máxima -> {list(entrada.keys())[indice_max]}: {valor_max}")
print(f"Nota mínima -> {list(entrada.keys())[indice_min]}: {valor_min}")
