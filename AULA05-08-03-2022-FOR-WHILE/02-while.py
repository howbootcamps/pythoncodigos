"""
How Bootcamps - Stone - /código[s]
Data: 10/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Estrutura de repetição (for e while)
"""

# Criando um dicionário vazio, que vai receber o nome como chave e uma lista de notas como valor
fechamento = dict()

# Recebe o nome do usuário
nome = input("Digite o nome do aluno: ")

# Inicia o dicinário com o nome do aluno com chave e uma lista vazia
fechamento[nome] = []

# Inicializa a condição para entrar na repetição while
condicao = "S"

# Enquanto a condição for "S"
while condicao == "S":

    # Lê uma nota do usuário
    nota = int(input("Digite uma nota: "))

    # Coloca essa nota na lista
    fechamento[nome].append(nota)

    # Pergunta se o usuário quer cadastrar mais notas (atualiza a condição)
    # Atenção ao .upper() ao final!
    condicao = input("Deseja entrar com mais uma nota? S ou N? ").upper()

    # Se a condição tiver uma única lera e for "S"
    if len(condicao) == 1 and condicao == "S":

        # Continua o laço de repetição
        continue

    # Caso a condição tenha uma letra e for "N"
    elif len(condicao) == 1 and condicao == "N":

        # Interrompe o laço
        break

    # Em todos os outros casos diferente dos acima
    else:
        # Pede para o usuário digitar uma opção válida
        print("Condição inválida! Digite uma condição válida!")

        # Lê novamente a condição
        condicao = input("Deseja entrar com mais uma nota? S ou N? ")
