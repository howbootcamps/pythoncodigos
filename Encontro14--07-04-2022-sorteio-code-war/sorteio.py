import csv
from collections import defaultdict
from random import choice

# 2 equipes completas ganham da stone
# 1 equipe completa ganha da how
# 3 ganham da stone individual

equipes = defaultdict(list)

with open("Sorteio.csv", encoding="utf-8") as csvfile:
    arquivo = csv.reader(csvfile, delimiter=";", quotechar="|")
    for linha in arquivo:
        nome_aluno = linha[1].strip().replace("  ", " ")
        numero_equipe = linha[0]
        equipes[numero_equipe].append(nome_aluno)

# 1 - 40 -> 2 sorteios Stone
# 1 - 40 -> 1 sorteios How
# 3 pessoas -> 3 brindes individuais da Stone

# 2 equipes
for _ in range(2):

    print("Sorteio do brinde da Stone!")

    equipe_sorteada = choice(list(equipes.keys()))
    pessoas_sorteadas = equipes[equipe_sorteada]

    print(f"A equipe sorteada foi {equipe_sorteada}...")

    for pessoa in pessoas_sorteadas:
        print(f"\nParabéns {pessoa}, você ganhou um brinde da Stone!")

    equipes.pop(equipe_sorteada)
    print("*" * 60)


# 1 equipe
print("Sorteio do brinde da How!")
equipe_sorteada = choice(list(equipes.keys()))
pessoas_sorteadas = equipes[equipe_sorteada]

print(f"A equipe sorteada foi {equipe_sorteada}...")

# 3 sorteios individuais
for pessoa in pessoas_sorteadas:
    print(f"\nParabéns {pessoa}, você ganhou um brinde da How!")

equipes.pop(equipe_sorteada)
print("*" * 60)

pessoas_nao_sorteadas = []

for lista_nomes in equipes.values():
    pessoas_nao_sorteadas.extend(lista_nomes)

print("Sorteio individual do brinde da Stone! \o/")

# 3 sorteios individuais
for _ in range(3):

    pessoa_sortuda = choice(pessoas_nao_sorteadas)

    pessoa_sortuda_indice = pessoas_nao_sorteadas.index(pessoa_sortuda)

    print(f"Parabéns {pessoa_sortuda}! Você ganhou um brinde individual!")

    pessoas_nao_sorteadas.pop(pessoa_sortuda_indice)
