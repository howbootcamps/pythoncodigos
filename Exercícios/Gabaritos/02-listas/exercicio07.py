"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.
"""
### PARTE N° 1 - CONVERTER LISTA DE STR PARA INT

# Solução n° 1 - usando a função `map`
# Obs: mais difícli de fazer, escreve menos código, precisa pesquisar mais do que o facilitador passou nos encontros...)

lista_string = ["1", "7", "99", "15"]

# Usamos a função `map` que aplica uma função, `int` no caso, à todos os elementos da lista
# A função `map` retorna um objeto do tipo `map`, transformamos esse objeto para lista com `list`
# Documentação oficial da função `map`: https://docs.python.org/3/library/functions.html#map
lista_string_convertida_1 = list(map(int, lista_string))

print(
    f"Lista de strings convertidas para inteiros - solução número 1: {lista_string_convertida_1}"
)

# Forma n° 2: usando loop for

lista_string_convertida_2 = []

for elemento in lista_string:

    # Transforma o elemento para inteiro
    elemento_int = int(elemento)

    # Adiciona na lista criada
    lista_string_convertida_2.append(elemento_int)

print(
    f"Lista de strings convertidas para inteiros - solução número 2: {lista_string_convertida_2}"
)

### PARTE N° 2 - CONVERTER LISTA DE INT PARA STR

# Usando somente a solução n° 2:

lista_int = [1, 7, 99, 15]

# Usamos a função `map` que aplica uma função, `str` no caso, à todos os elementos da lista
# A função `map` retorna um objeto do tipo `map`, transformamos esse objeto para lista com `list`
# Documentação oficial da função `map`: https://docs.python.org/3/library/functions.html#map
lista_int_convertida_1 = list(map(str, lista_int))

print(f"Lista de inteiros convertidos para string - solução número 1: {lista_int_convertida_1}")

# Experimentem fazer com a solução n° 2 também, é mais simples porém mais trabalhosa!
