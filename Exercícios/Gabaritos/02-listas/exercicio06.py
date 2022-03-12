"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Dada a seguinte lista lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] adicione o elemento 7000 logo após o elemento 6000 na lista. 
"""

lst = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

# Inicializa outra lista vazia, onde vamos colocar as strings que não são vazias
lst_sem_str_vazias = []

# Laço para percorrer todas as palavras da lista, incluindo as strings vazias
for palavra in lst:

    # Se a string não for vazia (sim, isso é uma condição!)
    if palavra:

        # Adiciona a palavra à lista de strings não vazias
        lst_sem_str_vazias.append(palavra)

print(lst_sem_str_vazias)
