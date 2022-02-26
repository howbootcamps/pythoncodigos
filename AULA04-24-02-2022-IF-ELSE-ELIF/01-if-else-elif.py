"""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Estrutura condicional (if, elif, else)
"""

aluno = "Henrique Branco"

# Criando uma lista vazia
notas = []

# Adicionando a primeira nota (input do usuário) à lista
notas.append(float(input("Digite a primeira nota: ")))

# Adicionando a segunda nota (input do usuário) à lista
notas.append(float(input("Digite a segunda nota: ")))

# Adicionando a terceira nota (input do usuário) à lista
notas.append(float(input("Digite a terceira nota: ")))

# Calculando a média das notas (não temos nenhuma função pronta!)
nota_media = sum(notas) / len(notas)

# Definindo padrões de aprovação
nota_minima_aprovacao = 7
nota_minima_rec = 6

# Verificação de aprovação do aluno
if nota_media >= nota_minima_aprovacao:
    status = "aprovado"

# Verificação de reprovação ou recuperação, caso aluno não tenha sido aprovado
elif nota_media >= nota_minima_rec:

    ## Chance de eliminar a nota mais baixa

    # Nota mínima
    nota_minima = min(notas)

    # Índice da nota mínima na lista
    nota_minima_indice = notas.index(nota_minima)

    # Eliminando a nota mínia através do seu índice
    notas.pop(nota_minima_indice)

    # Recalcula a média
    nota_media = sum(notas) / len(notas)

    # Define o status do aluno com a nova média
    if nota_media >= nota_minima_aprovacao:
        status = f"aprovado com {len(notas)}"
    else:
        status = "recuperação"

# Se nenhuma das condições acima foi atendida, então o aluno está reprovado!
else:
    status = "reprovado"

# Arredondando a média para 2 casas decimais
nota_media_arred = round(nota_media, 2)

# Imprime o resultado final na tela
print(f"\nA média do aluno {aluno} é {nota_media_arred} e este aluno tem o seguinte status: {status}")
