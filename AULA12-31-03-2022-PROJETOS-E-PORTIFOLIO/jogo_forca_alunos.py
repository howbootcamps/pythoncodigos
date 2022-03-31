"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.

Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

# from random import ?


def get_secret_word():
    """Devolve uma palavra aleatória de uma lista."""
    ...


def print_game_board():
    """Imprime a situação atual do jogo."""
    ...


def read_input_player():
    """Lê uma letra do usuário."""
    ...


def guess_letter():
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
    ...


def game_continue():
    """Função que decide se jogo já encerrou ou não."""
    ...


# secret_word = ? # variável para palavra secreta
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

while game_continue():
    print_game_board()
    read_input_player()
    guess_letter()
