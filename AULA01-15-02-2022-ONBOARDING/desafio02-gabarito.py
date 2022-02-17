"""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Henrique Junqueira Branco
Enunciado: 
O programa lê do usuário duas quantidades, dias e quilômetros. 
Considera-se que o preço por dia seja R$60 e que o preço por quilômetro rodado seja R$0.65.
Calcula-se o preço total do aluguel de um veículo e imprime-o na tela, formatando a saída com 7 dígitos e 2 casas decimais.
"""

# Desafio 02 - gabarito

qtd_km = int(input("Digite a quantidade de quilometros percorridos: "))

qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")
