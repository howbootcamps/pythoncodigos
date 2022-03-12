"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas posições. 
"""

lst = [5, 4, 6, 8, 3, 4]

maior = max(lst)
menor = min(lst)

posicao_maior = lst.index(maior)
posicao_menor = lst.index(menor)

print(f"O maior elemento é o {maior} e está na posição {posicao_maior}")
print(f"O menor elemento é o {menor} e está na posição {posicao_menor}")
