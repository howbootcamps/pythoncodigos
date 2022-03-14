"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""

A = int(input("Digite o primeiro número: "))

B = int(input("Digite o segundo número: "))

if A % B == 0:
    print(f"{A} é divisível por {B}")
else:
    print(f"{A} não é divisível por {B}")
