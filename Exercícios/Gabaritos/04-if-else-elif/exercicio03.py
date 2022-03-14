"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. 
Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo.

Obs: tabela no enunciado do exercício
"""

db = int(input("Digite um valor em decibéis (dB): "))

if db == 130:
    print("Valor sonoro de uma britadeira.")
elif 106 < db < 130:
    print("Valor sonoro entre britadeira e cortador de grama.")
elif db == 106:
    print("Valor sonoro de um cortador de grama.")
elif 70 < db < 106:
    print("Valor sonoro entre cortador de grama e despertador.")
elif db == 70:
    print("Valor sonoro de um despertador.")
elif 40 < db < 70:
    print("Valor sonoro entre despertador e cômodo silencioso.")
elif db == 70:
    print("Valor sonoro de um cômodo silencioso.")
elif db < 70:
    print("Valor sonoro abaixo de um cômodo silencioso.")
else:
    print("Valor sonoro acima de uma britadeira.")
