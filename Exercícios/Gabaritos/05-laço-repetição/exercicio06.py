"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
"""

N = int(input("Digite o valor de N: "))

H = 0

# Variável i começa em i e vai até N.
# Como range não conta a variável N, soma-se 1 à ela.
for i in range(1, N + 1):
    H += 1 / i

print(H)
