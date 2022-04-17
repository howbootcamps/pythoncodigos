"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco
Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.
Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""

# Sem dicas agora! Tentem elaborar toda a lógica do zero!

import itertools

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for c in itertools.permutations(numeros, r=9):

    soma_primeira_linha = c[0] + c[1] + c[2]
    soma_segunda_linha = c[3] + c[4] + c[5]
    soma_terceira_linha = c[6] + c[7] + c[8]

    soma_primeira_colua = c[0] + c[3] + c[6]
    soma_segunda_colua = c[1] + c[4] + c[7]
    soma_terceira_colua = c[2] + c[5] + c[8]

    soma_diagonal = c[0] + c[4] + c[8]
    soma_segunda_diagonal = c[2] + c[4] + c[6]

    set_somas = set(
        [
            soma_primeira_linha,
            soma_segunda_linha,
            soma_terceira_linha,
            soma_primeira_colua,
            soma_segunda_colua,
            soma_terceira_colua,
            soma_diagonal,
            soma_segunda_diagonal,
        ]
    )

    if (len(set_somas) == 1) and list(set_somas)[0] == 15:
        print("Temos um quadrado mágico!")
        print(c)
