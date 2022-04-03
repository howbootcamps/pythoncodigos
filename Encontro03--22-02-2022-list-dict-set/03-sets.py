"""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução aos tipos de dados - sets
"""

### INTRODUÇÃO BÁSICA

## Característica dos sets:
# Conjuntos matemáticos (sim, aquelas bolinhas com intersecção no meio!)
# Não há como acessar por posição (posições são aleatórias)
# Elementos únicos, exclusivos, sem repetição

## Formas de se criar um set
# Usando a notação {}
# Percebam que é diferente de um dicionário, pois dict tem {} : e , separando as chaves e valores
conjunto_a = {1,2,3,4,1,2,3,4,1,2,3,4}
print(f"Conjunto A: {conjunto_a}")

# Podemos usar a função set() para transformar outros objetos em um set
facilitador = set("Henrique Alves") # Transformando uma string para um set (sem letras repetidas)

# Fazendo a mesma coisa com outra string
letras_aleatorias = set("HeibfnAs ") # reparem no espaço ao final

# ----------------------------------------------------------------------------------------------------
### O PODER DOS SETS: COMPARANDO CONJUNTOS!

# Pergunta 1: Quais letras em comum temos em `facilitador` e `letras_aleatorias`?
print(f"Resp 1: {facilitador.intersection(letras_aleatorias)}")

# Pergunta 2: Quais letras temos em `facilitador` que não estão em `letras_aleatorias`?
print(f"Resp 2: {facilitador - letras_aleatorias}")

# Pergunta 3: Quais letras temos em `letras_aleatorias` que não estão em `facilitador`?
print(f"Resp 3: {letras_aleatorias - facilitador}")

# Pergunta 4: Quantas letras não repetidas temos ao total, quando consideramos `facilitador` e `letras_aleatorias`?
print(f"Resp 4: {len(facilitador.union(letras_aleatorias))}")

# Pergunta 5: Quais letras estão ou em `letras_aleatorias` ou em `facilitador` mas não em ambos ao mesmo tempo?
print(f"Resp 5: {facilitador.symmetric_difference(letras_aleatorias)}")

# Pergunta 6: A letra F está em `facilitador`
print(f"Resp 6: {'F' in facilitador}")

# Pergunta 7: `letras_aleatorias` é um subconjunto de `facilitador`? 
# Em outras palavras, `letras_aleatorias` está contida em `facilitador`?
# ou ainda: `facilitador` contém TODAS as letras de `letras_aleatorias`?
print(f"Resp 7: {letras_aleatorias.issubset(facilitador)}")

# e assim por diante! Pensou em conjunto, comparação de conjunto pensou em sets!!!