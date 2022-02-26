"""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução aos tipos de dados - listas
"""

### INTRODUÇÃO BÁSICA

## Listas começam com []
notas = [4,5,0,9,10]
print(f"Notas: {notas}")

## Podemos transformar outros objetos para o tipo lista com a função list()
notas_tup= (1,2,3,4) # Aqui criamos uma tupla
notas = list(notas_tup) # ... e transformamos o tipo de objeto de tupla para lista
print(f"A variável notas é do tipo: {type(notas)}") # Vamos checar com a função type()?

## Uma lista pode armazenar vários tipos de objetos
# Abaixo uma lista com string, int, float, booleano, e inclusive outra lista
lst_obj_variados = ["Henrique", 1, 10.0, False, [5,5,5]]
print(f"Lista com tipos de objetos variados: {lst_obj_variados}")

## Comprimento de lista
# A lista interna conta como um único elemento!
print(f"A lista `lst_obj_variados` tem {len(lst_obj_variados)} elementos")

# ----------------------------------------------------------------------------------------------------
### ACESSANDO ELEMENTOS DE LISTA COM FATIAMENTO (SLICING)

#########################################
# INDEXAÇÃO EM PYTHON COMEÇA POR ZERO!!!!
#########################################

# Acessando o primeiro elemento da lista
primeiro_elemento = lst_obj_variados[0]
print(f"\nO primeiro elemento da lista é {primeiro_elemento}")

# Obs: não confundir o [] de indexação (linha 35) com o [] de criação de listas (linha 11)!
# Indexação serve para coletar elementos de outros objetos (tuplas, strings) também usando []...

# Acessando o segundo elemento da lista
segundo_elemento = lst_obj_variados[1]
print(f"\nO segundo elemento da lista é {segundo_elemento}")

# A indexação pode ser na ordem inversa também (da direita para esquerda)
# Basta passar números negativos
ultimo_elemento  = lst_obj_variados[-1]
penultimo_elemento = lst_obj_variados[-2]
print(f"\nO último elemento da lista é {ultimo_elemento} e o penúltimo é {penultimo_elemento}")

# ----------------------------------------------------------------------------------------------------
### MÉTODOS MAIS COMUNS DE LISTA

# Adicionando um objeto inteiro ao final da lista
lst_obj_variados.append([9,9,9])
print(f"\nO elemento [9,9,9] foi adicionado ao final da lista: {lst_obj_variados}")

# Adicioando elemento a elemento de um objeto à lista
lst_obj_variados.extend("Henrique Branco")
print(f"\nCada letra da string foi adicionada como um elemento à lista: {lst_obj_variados}")

# Adicionando um objeto inteiro em uma determinada posição
lst_obj_variados.insert(0, "Index 0")
print(f"\nA string foi adicionada na primeira posição da lista, de índice 0: {lst_obj_variados}")

# Removendo o primeiro elemento encontrado da lista, retorna erro se não encontrar o elemento
lst_obj_variados.remove([9,9,9])
print(f"\nO objeto [9,9,9] agora foi removido da lista: {lst_obj_variados}")

# Coletando um elemento da lista e salvando em uma variável a partir de um índice
# O .pop() permite salvar o elemento removido em uma variável, o .remove() não permite!
elemento_coletado = lst_obj_variados.pop(0)
print(f"\nO elemento no índice 0 foi removido da lista: {lst_obj_variados}")
print(f"\nO elemento coletado é {elemento_coletado}")

# Ordenando os valores de uma lista
notas.sort() # Lista de notas (linha 11)
print(f"Notas ordenadas: {notas}")

# ...e a lista vai longe! Aqui são só alguns que abordamos nas aulas!
# temos ainda o .clear(), .copy(), .reverse()
