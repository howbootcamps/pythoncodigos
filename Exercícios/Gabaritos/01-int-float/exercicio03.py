"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
No exercício 02 você calculou a área de um triângulo a partir da sua base e altura. Faça um programa que receba os 3 lados de um triângulo (s1, s2 e s3) e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.
"""

s1 = float(input("Digite o primeiro lado do triângulo: "))

s2 = float(input("Digite o segundo lado do triângulo: "))

s3 = float(input("Digite o terceiro lado do triângulo: "))

# Fórmula no enunciado (arquivo word)
s = (s1 + s2 + s3) / 2

# Fórmula no enunciado (arquivo word)
area = (s * (s - s1) * (s - s2) * (s - s3)) ** (1 / 2)

print(f"A área do triângulo é {area}")
