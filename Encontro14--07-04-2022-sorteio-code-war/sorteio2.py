from random import randint, seed

seed(888)

numeros_sorteados = []

for _ in range(18):
    n = randint(1, 89)
    if n not in numeros_sorteados:
        numeros_sorteados.append(n)

for s in sorted(numeros_sorteados):
    print(s)

# 11 - Henrique César
# 23 - Ricardo Silveira
# 35 - Iara Varjão Barbosa
# 48 - Maly
# 49 - Flávia Fernandes dos Santos
# 50 - Lyndalee
# 51 - Thalita Peireira de Assis Pontes
# 54 - Rafael Pires Paes Leme
# 56 - Lucas Nascimento
# 57 - Pedro Henrique Birindiba
# 64 - Pedro Henrique Prestos Conceição
# 70 - Marcos Antônio Barros Lisboa
# 75 - Anderson Steves de Maceda
# 81 - Heitor de Pinho Freitas
# 82 - Danilson Macedo Perez

# Sorteio do Léo
# 27 - Lucas Matos de Lima Sobral
# 65 - Marcelo Lopes Valério
# 73 - Eliabe Gustavo Mendes
