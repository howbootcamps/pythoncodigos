"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Faça um programa que receba dois números inteiros do usuário, A e B e imprima na tela as seguintes operações:
1)	A soma de A e B;
2)	A diferença quando se subtrai B de A;
3)	O produto (multiplicação) entre A e B;
4)	O quociente (parte inteira da divisão) quando se divide A por B;
5)	O resto da divisão entre A e B;
6)	O resultado de log10 de A;
7)	O resultado de A elevado a B;
"""

from math import log10

A = int(input("Digite o número A: "))

B = int(input("Digite o número B: "))

print(f"1) {A + B}")

print(f"2) {B - A}")

print(f"3) {A * B}")

print(f"4) {A // B}")

print(f"5) {A % B}")

print(f"6) {log10(A)}")

print(f"7) {A ^ B}")