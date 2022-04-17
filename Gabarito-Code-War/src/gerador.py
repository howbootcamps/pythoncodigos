import random
from src import constantes

# Constantes

LABIRINTO = []
PAREDES = []

# Funções


def gera_labirinto(altura, largura):
    for i in range(altura):
        linha = []
        for j in range(largura):
            linha.append(constantes.SIM_NAO_VISITADO)
        LABIRINTO.append(linha)


def quantos_caminhos_vizinhos(posicao):
    quantidade = 0
    for movimento in constantes.MOVIMENTOS_POSSIVEIS:
        if LABIRINTO[posicao[0] + movimento[0]][posicao[1] + movimento[1]] == constantes.SIM_CAMINHO:
            quantidade += 1
    return quantidade

# Cria um labirinto, com as dimensões passadas como parâmetro.
# Nesse momento, o labirinto ainda não foi visitado.


def gerar():
    altura = int(input("Qual altura do seu labirinto? \n"))
    largura = int(input("Qual a largura do seu labirinto? \n"))
    gera_labirinto(altura, largura)

    # Defina um começo aleatório
    posicao_inicial = [random.randint(
        0, altura - 1), random.randint(0, largura - 1)]

    # Não deixe o caminho inicial ser na borda (fora do labirinto).
    if posicao_inicial[0] == 0:
        posicao_inicial[0] += 1
    if posicao_inicial[1] == 0:
        posicao_inicial[1] += 1
    if posicao_inicial[0] == altura - 1:
        posicao_inicial[0] -= 1
    if posicao_inicial[1] == largura - 1:
        posicao_inicial[1] -= 1

    # Transforme o ponto inicial em um caminho
    LABIRINTO[posicao_inicial[0]][posicao_inicial[1]] = constantes.SIM_CAMINHO

    # Envolva o ponto inical com paredes
    for movimento in constantes.MOVIMENTOS_POSSIVEIS:
        LABIRINTO[posicao_inicial[0] + movimento[0]
                  ][posicao_inicial[1] + movimento[1]] = constantes.SIM_PAREDE
        PAREDES.append([posicao_inicial[0] + movimento[0],
                       posicao_inicial[1] + movimento[1]])

    while PAREDES:
        # Escolha um movimento aleatório
        parede_aleatoria = random.choice(PAREDES)

        if (parede_aleatoria[1] != 0):
            if LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]-1] == constantes.SIM_NAO_VISITADO and LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]+1] == constantes.SIM_CAMINHO:
                qtd_vizinhos = quantos_caminhos_vizinhos(parede_aleatoria)
                if (qtd_vizinhos < 2):
                    LABIRINTO[parede_aleatoria[0]
                              ][parede_aleatoria[1]] = constantes.SIM_CAMINHO
                    if (parede_aleatoria[0] != 0):
                        if (LABIRINTO[parede_aleatoria[0]-1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] -
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]-1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]-1, parede_aleatoria[1]])
                    if (parede_aleatoria[0] != altura-1):
                        if (LABIRINTO[parede_aleatoria[0]+1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] +
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]+1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]+1, parede_aleatoria[1]])
                    if (parede_aleatoria[1] != 0):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]-1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]-1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]-1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]-1])

                for parede in PAREDES:
                    if (parede[0] == parede_aleatoria[0] and parede[1] == parede_aleatoria[1]):
                        PAREDES.remove(parede)
                continue

        if (parede_aleatoria[0] != 0):
            if (LABIRINTO[parede_aleatoria[0]-1][parede_aleatoria[1]] == constantes.SIM_NAO_VISITADO and LABIRINTO[parede_aleatoria[0]+1][parede_aleatoria[1]] == constantes.SIM_CAMINHO):
                qtd_vizinhos = quantos_caminhos_vizinhos(parede_aleatoria)
                if (qtd_vizinhos < 2):
                    LABIRINTO[parede_aleatoria[0]
                              ][parede_aleatoria[1]] = constantes.SIM_CAMINHO
                    if (parede_aleatoria[0] != 0):
                        if (LABIRINTO[parede_aleatoria[0]-1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] -
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]-1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]-1, parede_aleatoria[1]])
                    if (parede_aleatoria[1] != 0):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]-1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]-1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]-1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]-1])
                    if (parede_aleatoria[1] != largura-1):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]+1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]+1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]+1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]+1])

                for parede in PAREDES:
                    if (parede[0] == parede_aleatoria[0] and parede[1] == parede_aleatoria[1]):
                        PAREDES.remove(parede)
                continue

        if (parede_aleatoria[0] != altura-1):
            if (LABIRINTO[parede_aleatoria[0]+1][parede_aleatoria[1]] == constantes.SIM_NAO_VISITADO and LABIRINTO[parede_aleatoria[0]-1][parede_aleatoria[1]] == constantes.SIM_CAMINHO):
                qtd_vizinhos = quantos_caminhos_vizinhos(parede_aleatoria)
                if (qtd_vizinhos < 2):
                    LABIRINTO[parede_aleatoria[0]
                              ][parede_aleatoria[1]] = constantes.SIM_CAMINHO
                    if (parede_aleatoria[0] != altura-1):
                        if (LABIRINTO[parede_aleatoria[0]+1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] +
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]+1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]+1, parede_aleatoria[1]])
                    if (parede_aleatoria[1] != 0):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]-1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]-1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]-1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]-1])
                    if (parede_aleatoria[1] != largura-1):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]+1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]+1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]+1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]+1])

                for parede in PAREDES:
                    if (parede[0] == parede_aleatoria[0] and parede[1] == parede_aleatoria[1]):
                        PAREDES.remove(parede)
                continue

        if (parede_aleatoria[1] != largura-1):
            if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]+1] == constantes.SIM_NAO_VISITADO and LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]-1] == constantes.SIM_CAMINHO):
                qtd_vizinhos = quantos_caminhos_vizinhos(parede_aleatoria)
                if (qtd_vizinhos < 2):
                    LABIRINTO[parede_aleatoria[0]
                              ][parede_aleatoria[1]] = constantes.SIM_CAMINHO
                    if (parede_aleatoria[1] != largura-1):
                        if (LABIRINTO[parede_aleatoria[0]][parede_aleatoria[1]+1] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0]
                                      ][parede_aleatoria[1]+1] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0], parede_aleatoria[1]+1] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0], parede_aleatoria[1]+1])
                    if (parede_aleatoria[0] != altura-1):
                        if (LABIRINTO[parede_aleatoria[0]+1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] +
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]+1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]+1, parede_aleatoria[1]])
                    if (parede_aleatoria[0] != 0):
                        if (LABIRINTO[parede_aleatoria[0]-1][parede_aleatoria[1]] != constantes.SIM_CAMINHO):
                            LABIRINTO[parede_aleatoria[0] -
                                      1][parede_aleatoria[1]] = constantes.SIM_PAREDE
                        if ([parede_aleatoria[0]-1, parede_aleatoria[1]] not in PAREDES):
                            PAREDES.append(
                                [parede_aleatoria[0]-1, parede_aleatoria[1]])

                for parede in PAREDES:
                    if (parede[0] == parede_aleatoria[0] and parede[1] == parede_aleatoria[1]):
                        PAREDES.remove(parede)
                continue

        for parede in PAREDES:
            if (parede[0] == parede_aleatoria[0] and parede[1] == parede_aleatoria[1]):
                PAREDES.remove(parede)

    # Crie paredes aonde não foi visitado nesse momento
    for i in range(0, altura):
        for j in range(0, largura):
            if (LABIRINTO[i][j] == constantes.SIM_NAO_VISITADO):
                LABIRINTO[i][j] = constantes.SIM_PAREDE

    # Crie a saida do Labirinto
    for i in range(largura-1, 0, -1):
        if (LABIRINTO[altura-2][i] == constantes.SIM_CAMINHO):
            LABIRINTO[altura-1][i] = constantes.SAIDA
            break

    return LABIRINTO, posicao_inicial
