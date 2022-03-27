"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Um determinado zoológico cobra a entrada com base na idade do visitante.
Os visitantes com 2 anos de idade ou menos não pagam para entrar.
Crianças entre 3 e 12 anos custa R$14,00.
Idosos com 65 anos ou mais custam R$18,00.
A entrada para todos os outros visitantes é de R$23,00.
Crie um programa que comece lendo do usuário as idades de todos os visitantes de um determinado grupo, com uma idade inserida em cada linha.
O usuário digitará uma linha em branco para indicam que não há mais visitantes no grupo.
Em seguida, seu programa deve exibir o custo de admissão para o grupo com uma mensagem apropriada.
O custo deve ser exibido usando duas casas decimais.
"""

continuar = True

preco_final = 0.0

print("Digite as idades para adicionar integrantes ao grupo...")
print("... ou pressione enter para deixar em branco e encerrar!")

while continuar:
    idade = input("Digite uma idade para continuar: ")

    if not idade:
        continuar = False

    else:
        idade = int(idade)

        if 3 <= idade <= 12:
            preco_final += preco_final + 14
        elif 13 <= idade <= 64:
            preco_final += preco_final + 23
        elif 65 <= idade:
            preco_final += preco_final + 18

print(f"O preço final do grupo é R${preco_final:.2f}")
