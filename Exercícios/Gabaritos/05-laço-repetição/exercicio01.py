"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Neste exercício, você criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e imprime-a na tela. 
O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.
Atenção!
Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!
"""

lista_valores = []

while 0 not in lista_valores:
    valor = float(input("Digite um valor (ou digite 0 para encerrar a entrada de valores): "))

    if valor != 0:
        lista_valores.append(valor)
    else:
        break

if not lista_valores:
    print("Não encontrei nenhum valor na lista!")

else:
    print(f"A média dos valores calculados é: {sum(lista_valores) / len(lista_valores)}")
