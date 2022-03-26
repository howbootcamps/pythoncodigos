"""
How Bootcamps - Stone - /código[s]
Data: 22/03/2022
Autor: Henrique Junqueira Branco
Enunciado: 

A superfície da Terra é curva, e a distância entre os graus de longitude varia com a latitude.
Como resultado, encontrar a distância entre dois pontos na superfície da Terra é mais complicado do que simplesmente usar o teorema de Pitágoras.
Sejam (t1, g1) e (t2, g2) a latitude e a longitude de dois pontos na superfície da Terra.
A distância entre esses pontos, acompanhando a superfície da Terra, em quilômetros é:

distancia = 6371,01 x arccos(sen(t1) x sen(t2) + cos(t1) x cos(t2) x cos(g1 - g2))

O valor 6371,01 na equação anterior não foi selecionado aleatoriamente. 
É o raio médio da Terra em quilômetros.

Crie um programa que permita ao usuário inserir a latitude e longitude de dois pontos da Terra em graus.
Seu programa deve exibir a distância entre os pontos, seguindo a superfície da terra, em quilômetros.

Dica¹: as funções trigonométricas do Python operam em radianos. 
Como resultado, você vai precisa converter a entrada do usuário de graus para radianos antes de calcular a distância com a fórmula discutida anteriormente. 
O módulo math contém um função chamada radianos que converte de graus para radianos.

Dica²: 
Latitude varia de -90° (sul) até +90° (norte). O ponto de latitude 0° é a linha do equador
Longitude varia de -180° (leste) até +180° (oeste). O ponto de longitude 0° é o meridiano de Greenwich
"""

from math import acos, cos, radians, sin

print("Primeiro ponto: ")
coord_str = input("Digite a primeira coordenada em graus sem espaços separadas por vírgula: ")
coord_lista_str = coord_str.split(",")
t1, g1 = list(map(float, coord_lista_str))

t1 = radians(t1)
g1 = radians(g1)

print("Segundo ponto: ")
t2 = radians(float(input("Digite a latitude em graus: ")))
g2 = radians(float(input("Digite a longitude em graus: ")))

# distancia = 6371,01 x arccos(sen(t1) x sen(t2) + cos(t1) x cos(t2) x cos(g1 - g2))
distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print(f"A distância em quilômetros calculada é: {distancia}")

# t1 = -20.8480435
# g1 = -49.3872444

# t2 = -25.4947402
# g2 = -49.4298817

# ~700 km
