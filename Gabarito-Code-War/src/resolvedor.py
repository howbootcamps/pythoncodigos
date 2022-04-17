import os
import sys
from time import sleep
from src import constantes


CAMINHO = []


def print_labirinto(labirinto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    for linha in labirinto:
        print("".join(linha))
    print("")


def movimento(labirinto, posicao: tuple, movimento: list, voltar=False):
    caminho = constantes.SIM_CAMINHO if voltar else constantes.CAMINHO_PERCORRIDO

    labirinto[posicao[0]][posicao[1]] = caminho
    labirinto[posicao[0] + movimento[0]][posicao[1] + movimento[1]] = constantes.ROBO

    if voltar:
        CAMINHO.append(posicao)

    return [posicao[0] + movimento[0], posicao[1] + movimento[1]]


def verifica_movimento(labirinto, posicao: tuple, movimento: list, voltar=False) -> bool:
    if labirinto[posicao[0] + movimento[0]][posicao[1] + movimento[1]] == constantes.SAIDA:
        print("SUCESSO")
        sys.exit()

    caminho = labirinto[posicao[0] + movimento[0]][posicao[1] + movimento[1]]

    if voltar:
        return caminho == constantes.CAMINHO_PERCORRIDO
    else:
        nao_percorrido = [posicao[0] + movimento[0], posicao[1] + movimento[1]] not in CAMINHO
        return caminho == constantes.SIM_CAMINHO and nao_percorrido


def movimentar(labirinto, posicao_atual, movimentos):
    movimentou = False
    for m in movimentos:
        if verifica_movimento(labirinto, posicao_atual, m):
            posicao_atual = movimento(labirinto, posicao_atual, m)
            movimentou = True
            break

    if not movimentou:
        for m in movimentos:
            if verifica_movimento(labirinto, posicao_atual, m, True):
                posicao_atual = movimento(labirinto, posicao_atual, m, True)
                break

    print_labirinto(labirinto)
    sleep(constantes.VELOCIDADE)
    movimentar(labirinto, posicao_atual, movimentos)


def resolver(posicao_inicial, labirinto):
    labirinto[posicao_inicial[0]][posicao_inicial[1]] = constantes.ROBO
    print_labirinto(labirinto)

    movimentar(labirinto, posicao_inicial, constantes.MOVIMENTOS_POSSIVEIS)
