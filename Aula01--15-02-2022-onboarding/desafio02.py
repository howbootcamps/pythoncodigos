"""
How Bootcamps - Stone - /código[s]
Data: 15/02/2022
Autor: Henrique Junqueira Branco
Enunciado: exercício proposto na aula introdutória para elucidar a criatividade dos alunos e 
começarem a obter a perceção do que um código faz. O enunciado será escrito ao final da aula, ao 
vivo, após análise dos alunos.
"""

# Desafio 02: o que esse pequeno trecho de código faz?

qtd_km = int(input("Digite a quantidade de quilometros percorridos: "))

qtd_dias = int(input("Digite quantos dias você ficou com o carro:"))

preco_por_dia = 60
preco_por_km = 0.15

preco_total_km = qtd_km * preco_por_km
preco_total_dia = qtd_dias * preco_por_dia

preco_a_pagar = preco_total_km + preco_total_dia

print(f"Total a pagar: R$ {preco_a_pagar:7.2f}")
