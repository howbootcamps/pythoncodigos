"""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Autor: Henrique Junqueira Branco
Enunciado: funções
"""

# Definição da função para cálculo da média
# A função recebe uma lista como parâmetro e retorna um float
def calcula_media(lst: list) -> float:
    """Calcula a média aritimérica."""

    # Retorna o cálculo da média da lista
    return sum(lst) / len(lst)

# Função para cálculo da média ponderada
# A função recebe `valores` que é uma lista, `pesos` que é uma tupla e retorna um float
# O parâmetro valores é obrigatório
# O parâmetro pesos é opcional. Se não for passado:
#   * Criamos uma tupla com vários números de mesmo tamanho (número de elementos) do parâmetro `valores`
def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """Calcula a média ponderada."""

    # Se não for passado o parâmetro de pesos
    if not pesos:
        
        # Criamos uma tupla cheia de 1, com mesmo número de elementos de `valores`
        pesos = (1,) * len(valores)

    # Inicia uma soma acumulativa com zero
    numerador = 0

    # Soma dos pesos
    denominador = sum(pesos)

    # Iterando por cada par de valor, peso
    for valor, peso in zip(valores, pesos):

        # Soma cumulativa da multiplicação de cada valor por cada peso
        numerador = numerador + valor * peso
        
    # Retornando a média ponderada
    return numerador / denominador

# Criando um dicionário vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento = dict()

# Recebe do usuário quantos alunos serão cadastrados
numero_alunos = int(input("Querido usuário, quantos alunos serão? "))

# Recebe quantas notas por aluno serão cadastradas
numero_notas = int(input("Querido usuário, quantas notas por aluno? "))

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

    # Chamamos a função de cálculo de média ponderada, sem passar os pesos (opcional)
    media = calcula_media_ponderada(notas)

    # Imprime o nome do aluno e a média na tela
    print(f"A média do aluno {aluno} foi {media}!")
