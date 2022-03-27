"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado: 
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informadas ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

"""

notas = []

nome = input("Atleta: ")
for _ in range(7):
    nota = float(input("Nota: "))
    notas.append(nota)

maior_nota = max(notas)
indice_maior_nota = notas.index(maior_nota)
notas.pop(indice_maior_nota)

menor_nota = min(notas)
indice_menor_nota = notas.index(menor_nota)
notas.pop(indice_menor_nota)

print("Resultado final:")
print(f"Atleta: {nome}")
print(f"Melhor nota: {maior_nota}")
print(f"Pior nota: {menor_nota}")
print(f"Média: {sum(notas) / len(notas)}")
