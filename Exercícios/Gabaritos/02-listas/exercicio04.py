"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso)
"""

meses = (
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)


temperaturas = []

# Laço de repetição para ler as temperatudas dos meses
for mes in meses:

    # Lê a temperatura de cada mês
    temperatura = float(input(f"Digite a temperatura (°C) do mês de {mes}: "))

    # Adiciona na lista
    temperaturas.append(temperatura)

# Calcula a média anual das temperaturas, arredondando para 2 casas decimais
media_temp_anual = round(sum(temperaturas) / len(temperaturas), 2)

print(f"Meses com a temperatura acima da média anual de {media_temp_anual}°C:")

# Laço de repetição para percorrer todas as temperaturas e suas posições na lista
# Link da documentação oficial para função enumerate:
# https://docs.python.org/3/library/functions.html#enumerate
for indice, temp in enumerate(temperaturas):

    # Checagem se a temperatura é maior do que a média anual
    if temp > media_temp_anual:

        # Os índices começam por 0!
        # Para fazer com que os índices correspondam ao número dos meses, soma-se 1 ao índice
        # Janeiro no índice 0 é o mês 1
        # Fevereiro no índice 1 é o mês 2
        # e assim por diante...
        print(f"{indice+1} - {meses[indice]}")
