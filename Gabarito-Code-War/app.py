from src.gerador import gerar
from src.resolvedor import resolver

if __name__ == "__main__":
    labirinto, posicao_inicial = gerar()

    resolver(posicao_inicial, labirinto)
