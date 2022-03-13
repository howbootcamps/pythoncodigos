"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Escreva um programa que leia do usuário um número de 4 dígitos e imprima a soma destes dígitos. 
Exemplo, se o usuário digitar 3141 seu programa deverá imprimir na tela 3+1+4+1=9.
"""

numero = input("Digite um número de 4 dígitos: ")

# Enquanto a entrada não tiver 4 digitos ou todos eles não forem numéricos:
while len(numero) != 4 or not numero.isnumeric():

    # Solicita novamente um número ao usuário
    numero = input("Número inválido! Digite um número válido de 4 dígitos: ")

soma = int(numero[0]) + int(numero[1]) + int(numero[2]) + int(numero[3])

print(f"{numero[0]}+{numero[1]}+{numero[2]}+{numero[3]}={soma}")
