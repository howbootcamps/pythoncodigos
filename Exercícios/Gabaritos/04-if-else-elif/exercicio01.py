"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Escreva um programa que diga se um número dado pelo usuário é par ou ímpar.
"""

numero = int(input("Digite um número: "))

# Conceito de número par: se o resto da divisão por 2 for zero, então é par. Caso contrário, é ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
