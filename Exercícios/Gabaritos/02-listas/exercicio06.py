"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que remova strings vazias de uma lista de strings.

Exemplo:
dada a lista ["Olá", "", "meu", "nome", "", "é", "facilitador", ""] a saída deve ser
>> ["Olá", "meu", "nome", "é", "facilitador"]
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
