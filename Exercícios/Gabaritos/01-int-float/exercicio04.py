"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que receba do usuário seu peso em kg e altura em metros e imprima o Índice de Massa Corporal (IMC) do usuário.
"""

peso = float(input("Digite o seu peso em kg: "))

altura = float(input("Digite a sua altura em metros: "))

# Fórmula no enunciado (arquivo word)
imc = peso / (altura**2)

print(f"O IMC calculado é {imc}")
