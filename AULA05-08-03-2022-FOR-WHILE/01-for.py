"""
How Bootcamps - Stone - /código[s]
Data: 08/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Estrutura de repetição (for e while)
"""

# Criando um dicionário vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento = dict()

# Recebe do usuário quantos alunos serão cadastrados
numero_alunos = int(input("Querido usuário, quantos alunos serão? "))

# Recebe quantas notas por aluno serão cadastradas
numero_notas = int(input("Quantas notas por aluno? "))

# Laço de repetição para cadastro de alunos
for _ in range(numero_alunos):

    # Lê o nome do aluno
    nome = input("Digite o nome do aluno: ")

    # Cria no dicionário uma chave com o nome do aluno, e o valor sendo uma lista vazia
    fechamento[nome] = []

    # Laço de repetição para ler as notas do aluno
    for _ in range(numero_notas):

        # Lê a nota daquele aluno
        nota = int(input(f"Digite a nota do {nome}: "))

        # Coloca a nota na lista
        fechamento[nome].append(nota)

# Laço no dicionário para calcular a média de cada aluno e imprimir na tela
for aluno, notas in fechamento.items():

    # Calcula a média
    media = sum(notas) / len(notas)

    # Imprime o nome do aluno e a média na tela
    print(f"A média do aluno {aluno} foi {media}!")
