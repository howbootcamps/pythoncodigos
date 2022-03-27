"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita):

pi≈3+4/2x3x4-4/4x5x6+4/6x7x8-4/8x9x10+4/10x11x12-4/12x13x14+⋯

Escreva um programa que calcule o número pi com 15 aproximações. 
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. 
A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante!
"""

pi = 0

for aprox in range(15):
    if aprox == 0:
        pi += 3
        continue

    dobro_aprox = aprox * 2
    denominador = dobro_aprox * (dobro_aprox + 1) * (dobro_aprox + 2)

    if aprox % 2 != 0:
        pi += 4 / denominador
    else:
        pi -= 4 / denominador

print(f"O número pi com 15 aproximações é {pi}")
