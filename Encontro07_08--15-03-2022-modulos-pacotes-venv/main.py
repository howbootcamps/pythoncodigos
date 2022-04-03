"""
How Bootcamps - Stone - /código[s]
Data: 15/03/2022
Autor: Henrique Junqueira Branco
Enunciado: módulos
"""

from calculo import calcula_media_ponderada

fechamento = dict()

numero_alunos = int(input("Querido usuário, quantos alunos serão? "))
numero_notas = int(input("Querido usuário, quantas notas por aluno? "))

for _ in range(numero_alunos):

    nome = input("Digite o nome do aluno: ")

    fechamento[nome] = []

    for _ in range(numero_notas):

        nota = int(input(f"Digite a nota do {nome}: "))

        fechamento[nome].append(nota)


for aluno, notas in fechamento.items():
    media = calcula_media_ponderada(notas)
    print(f"A média do aluno {aluno} foi {media}!")
