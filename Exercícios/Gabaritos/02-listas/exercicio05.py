"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista. 
"""

lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Lembre-se: a indexação começa por 0!
# Passo 1. Primeiro acessamos o terceiro elemento (índice 2) da lista, que é o [300, 400, [5000, 6000], 500]
# Passo 2. Da lista do passo 1, selecionamos o terceiro elemento (índice 2) dessa lista, que é [5000, 6000]
# Passo 3. Finalmente, adicionamos o elemento 7000 à lista do passo 2
lst[2][2].append(7000)

print(lst)
