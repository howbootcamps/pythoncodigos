"""
How Bootcamps - Stone - /código[s]
Data: 17/02/2022
Autor: Henrique Junqueira Branco
Enunciado: Introdução aos tipos de dados (string)
"""

nome = "   henrique Alves Junqueira Nogueira Branco   "

### Métodos de string com a sintaxe nome.metodo()

print(f"Nome em maiúsculo: {nome.upper()}")

print(f"Nome em minúsculo: {nome.lower()}")

print(f"Primeira letra em maiúsculo: {nome.capitalize()}")

# Atenção às aspas duplas e simples! Comentamos isso na aula!
print(f"Contando quantas vezes a letra 'a' aparece no nome: {nome.count('a')}")

print(f"Removendo espaços em branco no começo e final da string: {nome.strip()}")

# Cuidado com as aspas de novo! Se misturar, dá ruim!
print(f"Substituindo meu nome por algo engraçado: {nome.replace('henrique', 'xpto')}")

print(f"Separando o nome em partes: {nome.split()}")

### Função len()

# Os espaços em branco contam, lembram?
print(f"A minha string contém {len(nome)} caracteres")