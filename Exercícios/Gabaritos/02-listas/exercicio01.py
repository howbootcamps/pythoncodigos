"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão). Imprima na tela o elemento e sua respectiva posição na lista. 
"""

lst = [1, 3, 6, "Uma string qualquer", [7, 7, 7]]

# Laço para iterar pelas posições e elementos da lista
# Link da documentação oficial para função enumerate:
# https://docs.python.org/3/library/functions.html#enumerate

for posicao, elemento in enumerate(lst):
    print(f"Elemento {elemento} na posição {posicao}")
