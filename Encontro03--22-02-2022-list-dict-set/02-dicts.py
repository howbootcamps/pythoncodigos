"""
How Bootcamps - Stone - /código[s]
Data: 24/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução aos tipos de dados - dicionários
"""

### INTRODUÇÃO BÁSICA

## Característica dos dicionários
# São estruturas de dados de mapeamento, de de-para, chave-valor
# Começam com {} e tem : que dividem os partes de chave:valor e vírgula separando um par de chave e valor do outro

sigla_estado = {"SP" : "São Paulo", "MG" : "Minas Gerais"}

# Podemos criar um dicionário idêntico com a função dict()
# Reparem que as chaves são passadas como parâmetros nomeados da função dict(), e não como string
# O resultado é o mesmo dicionário da linha 14
sigla_estado = dict(SP="São Paulo", MG="Minas Gerais")
print(f"Dicionário inicial: {sigla_estado}")

# ----------------------------------------------------------------------------------------------------
### ACESSANDO ELEMENTOS DE UM DICIONÁRIO

# Acessamos um valor de um dicionário a partir da sua chave usando a notação de []
print(f"\nO valor para a chave 'SP' é {sigla_estado['SP']}")

# Caso uma chave não exista, o código gera um erro. Descomente a linha 29 abaixo e execute o código
# KeyError: "RJ" -> Ela não existe no dicionário
# print(sigla_estado["RJ"])

# Podemos criar uma chave que não existe atribuindo um valor à ela
sigla_estado["RJ"] = "Rio de Janeiro"
print(f"\nA nova chave foi criada: {sigla_estado}")


# ----------------------------------------------------------------------------------------------------
### MÉTODOS MAIS COMUNS DE DICIONÁRIOS

# Alguns que não necessitam de exemplos são: clear() e copy()
# clear() limpa o dicionário e copy() cria uma cópia dele

# Retornando apenas as chaves do meu dicionário
print(f"\nTransformando as chaves em uma lista: {list(sigla_estado)}")
print(f"\nTransformando as chaves em um outro objeto: {sigla_estado.keys()}")

# Retornando os valores do meu dicionário
print(f"\nValores do meu dicionário: {sigla_estado.values()}")

# Retornando os pares de chave-valor
print(f"\nPares de chave-valor: {sigla_estado.items()}")

# ----------------------------------------------------------------------------------------------------
### CHECANDO EXISTENCIA DE ITENS NO DICIONÁRIO
check_sp = "SP" in sigla_estado
print(f"\nA sigla SP está nas chaves? Resposta: {check_sp}")

check_se = "SE" in sigla_estado
print(f"\nA sigla SE está nas chaves? Resposta: {check_se}")
